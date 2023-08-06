Release management
==================

* Prepare the ../release-notes.rst

* Prepare a new version

.. code:: sh

 $ version=1.3.0
 $ rm -f inventory/hosts.yml inventory/group_vars/all/clouds.yml
 $ perl -pi -e "s/^version.*/version = $version/" setup.cfg
 $ for i in 1 2 ; do
       python setup.py sdist
       amend=$(git log -1 --oneline | grep --quiet "version $version" && echo --amend)
       git commit $amend -m "version $version" ChangeLog setup.cfg
       git tag -a -f -m "version $version" $version
   done

* Build the release locally

.. code:: sh

 $ docker rmi enoughcommunity/enough
 $ python -m enough.internal.cmd build image
 $ docker tag enough:$version enoughcommunity/enough:latest
 $ docker tag enough:$version enoughcommunity/enough:$version
 $ docker rmi enough:$version

* (Optional) manual test the release

.. code:: sh

  $ eval "$(docker run --rm enoughcommunity/enough:latest install)"
  $ enough --version

* Publish the release

.. code:: sh

 $ git push ; git push --tags
 $ twine upload -s --username enough --password "$ENOUGH_PYPI_PASSWORD" dist/enough-$version.tar.gz
 $ docker login --username enoughh --password "$ENOUGH_DOCKER_HUB_PASSWORD"
 $ docker push enoughcommunity/enough:latest
 $ docker push enoughcommunity/enough:$version

* PyPI maintenance

  * if the project does not yet exist

    .. code:: sh

     $ python setup.py register
  * trim old versions at https://pypi.python.org/pypi/enough
