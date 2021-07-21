#!/bin/sh

while true;
do
{ echo -e 'HTTP/1.1 200 OK\r\n\r\n'; sleep 2; } | nc -l -p 9991;
done