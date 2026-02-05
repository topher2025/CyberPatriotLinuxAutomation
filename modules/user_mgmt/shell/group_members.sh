#!/bin/sh

getent group "$1" | awk -F: '{ print $4 }' | tr ',' '\n'
