#!/bin/bash
set -euo pipefail

OUTDIR="$1"
source ./version

fedpkg clone --anonymous --branch "$BRANCH" kernel
cd kernel
git switch --detach "$COMMIT"

fedpkg sources

sed --in-place "/^# define buildid /c\%define buildid .os" ./kernel.spec
for patch in ../patches/*.patch; do
  cat "$patch" >> ./linux-kernel-test.patch
done

fedpkg srpm
mv ./*.src.rpm "$OUTDIR/"
