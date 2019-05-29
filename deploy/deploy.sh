#!/bin/bash

APP_PATH="bin/app"

run_check_directory()
{
    rm -r check
    mkdir check
    cd check
    sleep 1
    url="https://dl.bintray.com/danimtb/helloworld/danimtb/Hello/1.0/testing/0/package/90ee443cae5dd5c1b4861766ac14dc6fae231a92/0/conan_package.tgz"
    wget "$url"
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
while [ 1 ]
do
    rm -r execute
    cp -r ./check ./execute
    cd execute
    $APP_PATH &
    app_pid=$!
    sleep 5
    deploy_content="$(read_binary_content execute)"
    check=1

    while [ $check -gt 0 ]
    do
        run_check_directory
        new_deploy_content="$(read_binary_content check)"

        if [ $deploy_content -ne $new_deploy_content ]; then
            kill -9 $app_pid
            check=0
        fi
    done
done
