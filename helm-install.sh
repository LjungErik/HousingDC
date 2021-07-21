#!/bin/bash

package_dir="packages/helm"
name=""
values_file=""
version=""
namespace="development"

usage(){
    echo "Usage: ./helm-install.sh [FLAGS]"
    echo " "
    echo "--name (REQUIRED): Name of charts to deploy"
    echo "--version (REQUIRED): Chart version"
    echo "-f (REQUIRED): The value.yaml file to use to overwrite values"
    echo "--namespace (OPTIONAL): namespace to deploy to, default: development"
    echo " "
}

while test $# -gt 0; do
    case "$1" in
      --name)
        shift
        if test $# -gt 0; then
            name=$1
        else
            echo "no specified name"
            usage
            exit 1
        fi
        shift
        ;;
        -v|--version)
        shift
        if test $# -gt 0; then
            version=$1
        else
            echo "no specified version"
            usage
            exit 1
        fi
        shift
        ;;
        -f)
        shift
        if test $# -gt 0; then
            values_file=$1
        else
            echo "no specified values file"
            usage
            exit 1
        fi
        shift
        ;;
        --namespace)
        shift
        if test $# -gt 0; then
            namespace=$1
        else
            echo "no specified namespace"
            usage
            exit 1
        fi
        shift
        ;;
        *)
        break
        ;;
    esac
done

APPVERSION=$(git rev-parse --short HEAD)

if [ -z $name ]; then
    echo "missing name"
    usage
    exit 1
fi 

if [ -z $version ]; then
    echo "missing version"
    usage
    exit 1
fi

if [ -z $values_file ]; then
    echo "missing values file"
    usage
    exit 1
fi

echo "Generating Helm package"
$chart_dir = "helm/$name"
helm package $chart_dir -d $package_dir --version $version --app-version $APPVERSION

if [ $? -eq 0 ]; then
    mkdir tmp
    echo "Unpackage generated helm"
    package="$package_dir/$name-collector-$version.tgz"
    tar zxf $package -C tmp

    echo "Install helm charts"
    release="$name-collector" 
    release_chart="tmp/$name"
    helm upgrade $release $release_chart -i -f $values_file --namespace $namespace

    rm -rf tmp
else
    echo "Failed to package helm chart"
    exit 1
fi
