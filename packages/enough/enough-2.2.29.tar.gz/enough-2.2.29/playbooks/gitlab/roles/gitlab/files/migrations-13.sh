set -ex

#
# It is not just for information: entrypoint.sh has side effects that
# allow the next commands to run successfully
#
/sbin/entrypoint.sh app:rake gitlab:env:info

# workaround migration bug to 14.9.2 https://gitlab.com/gitlab-org/gitlab/-/issues/353927#note_888445881
bundle exec rake RAILS_ENV=production db:migrate:up VERSION=20211123135255

bundle exec rake RAILS_ENV=production gitlab:background_migrations:finalize[CopyColumnUsingBackgroundMigrationJob,events,id,'[["id"]\, ["id_convert_to_bigint"]]']
bundle exec rake RAILS_ENV=production gitlab:background_migrations:finalize[CopyColumnUsingBackgroundMigrationJob,push_event_payloads,event_id,'[["event_id"]\, ["event_id_convert_to_bigint"]]']

bundle exec rake RAILS_ENV=production gitlab:background_migrations:finalize[CopyColumnUsingBackgroundMigrationJob,taggings,id,'[["id"\, "taggable_id"]\, ["id_convert_to_bigint"\, "taggable_id_convert_to_bigint"]]'] 
bundle exec rake RAILS_ENV=production gitlab:background_migrations:finalize[CopyColumnUsingBackgroundMigrationJob,ci_builds,id,'[["id"\, "stage_id"]\, ["id_convert_to_bigint"\, "stage_id_convert_to_bigint"]]']
bundle exec rake RAILS_ENV=production gitlab:background_migrations:finalize[CopyColumnUsingBackgroundMigrationJob,ci_job_artifacts,id,'[["id"\, "job_id"]\, ["id_convert_to_bigint"\, "job_id_convert_to_bigint"]]']
bundle exec rake RAILS_ENV=production gitlab:background_migrations:finalize[CopyColumnUsingBackgroundMigrationJob,ci_stages,id,'[["id"]\, ["id_convert_to_bigint"]]']
bundle exec rake RAILS_ENV=production gitlab:background_migrations:finalize[CopyColumnUsingBackgroundMigrationJob,ci_builds_metadata,id,'[["id"]\, ["id_convert_to_bigint"]]']
bundle exec rake RAILS_ENV=production gitlab:background_migrations:finalize[CopyColumnUsingBackgroundMigrationJob,ci_builds_metadata,id,'[["build_id"]\, ["build_id_convert_to_bigint"]]']

# Repeat because it may take a while for the tasks above to complete in the background
success=false
for i in $(seq 2) ; do
    sleep 5
    if bundle exec rake RAILS_ENV=production db:migrate ; then
	success=true
	break
    fi
    echo "remaining tasks count"
    /home/git/gitlab/bin/rails runner -e production 'puts Gitlab::BackgroundMigration.remaining'
    # https://docs.gitlab.com/ee/raketasks/sidekiq_job_migration.html#future-jobs
    # bundle exec rake RAILS_ENV=production gitlab:sidekiq:migrate_jobs:retry gitlab:sidekiq:migrate_jobs:schedule
    #
    # https://docs.gitlab.com/ee/update/index.html#batched-background-migrations
    #/home/git/gitlab/bin/rails c <<EOF
    #scheduled_queue = Sidekiq::ScheduledSet.new
    #pending_job_classes = scheduled_queue.select { |job| job["class"] == "BackgroundMigrationWorker" }.map { |job| job["args"].first }.uniq
    #pending_job_classes.each { |job_class| Gitlab::BackgroundMigration.steal(job_class) }
    #EOF
done
if $success ; then
    exit 0
else
    exit 5
fi
