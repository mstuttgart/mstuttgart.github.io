#!/usr/bin/env bash
BRANCH=pelican
TARGET_REPO=mstuttgart/mstuttgart.github.io.git
PELICAN_OUTPUT_FOLDER=output

echo -e "Testing travis-encrypt"
echo -e "$VARNAME"

if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
    echo -e "Starting to deploy to Github Pages\n"
    if [ "$TRAVIS" == "true" ]; then
        git config --global user.email "travis@travis-ci.org"
        git config --global user.name "Travis"
    fi
    # Using token clone gh-pages branch
    git clone --quiet --branch=$BRANCH https://${GH_TOKEN}@github.com/$TARGET_REPO built_website > /dev/null

    # Go into directory and copy data we're interested in to that directory
    cd built_website
    make github
    # rsync -rv --exclude=.git  ../$PELICAN_OUTPUT_FOLDER/* .

    # Add, commit and push files
    # git add -f .
    # git commit -m "Travis build $TRAVIS_BUILD_NUMBER pushed to Github Pages"
    # git push -fq origin $BRANCH > /dev/null
    echo -e "Deploy completed\n"
fi
