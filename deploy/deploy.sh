#!/bin/bash

REFERENCE="danimtb/Hello/0.1/testing"
APP_PATH="bin/app"

run_check_directory()
{
    rm -r check
    mkdir check
    cd check
    sleep 1
    url = "https://dl.bintray.com/danimtb/helloworld/$REFERENCE/0/package/6cc50b139b9c3d27b3e9042d5f5372d327b3a9f7/0/:conan_package.tgz"
    wget url
    tar -xzf conan_package.tgz
    cd ..
}

read_binary_content ()
{
    folder=$1
    binary_content=$(<$folder/$APP_PATH)
    return binary_content
}


run_check_directory
while
do
    rm -r execute
    cp -r ./check ./execute
    cd execute
    $APP_PATH &
    app_pid=$!
    sleep 5
    deploy_content="$(my_function execute)"
    check=1

    while [ $check -gt 0 ]
    do
        run_check_directory
        new_deploy_content="$(my_function check)"

        if [ $deploy_content -ne $new_deploy_content ]; then
            kill -9 $app_pid
            check=0
        fi
    done
done
