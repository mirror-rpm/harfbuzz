#!/bin/bash
cd ../source

echo "---Start autogen.sh---"
NOCONFIGURE=1 ./autogen.sh
echo "---End autogen.sh---"
echo "--------------------"

find . -type f -exec sed -i 's/env python/python3/g' {} \; && ./configure --disable-static --with-graphite2 && echo "--------------------"; echo "---Start make check---"; make check; echo "---End make check---"
