#! /bin/bash
set -eu

DIR=`dirname $0`
set -a; eval "$(cat $DIR/.env.development <(echo) <(declare -x) | grep -v '^#')"; set +a;
eval "$@"