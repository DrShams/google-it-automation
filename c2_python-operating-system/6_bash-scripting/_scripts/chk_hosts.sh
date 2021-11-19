#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
  echo "everything is ok"
else
  echo "error localhost is not here"
fi
