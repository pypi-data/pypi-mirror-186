#!/bin/bash
# SPDX-FileCopyrightText: (C) 2022 Avnet Embedded GmbH
# SPDX-License-Identifier: GPL-3.0-only

set -e

if [ $# -ne 3 ];
then
    echo "Usage ${0} vmname kernel disk_image"
    exit 2
fi

VMNAME="$1"
KERNEL="$2"
DISK="$3"
TMPDIR=$(mktemp -d)

KERNEL_PATH=$(realpath "${KERNEL}")
DISK_PATH=$(realpath "${DISK}")
KERNEL_FILENAME=$(basename "${KERNEL_PATH}")
DISK_FILENAME=$(basename "${DISK_PATH}")
SCRIPT_DIR=$(dirname "$(realpath "${0}")")

cp "${SCRIPT_DIR}/vm_create.sh.template" "${TMPDIR}/vm_create.sh"
sed -i "s/@@VMNAME@@/${VMNAME}/;s/@@KERNEL@@/${KERNEL_FILENAME}/;s/@@DISK@@/${DISK_FILENAME}/" "${TMPDIR}/vm_create.sh"
chmod +x "${TMPDIR}/vm_create.sh"

tar -cjpf "${VMNAME}_bundle.tar.bz2" "${KERNEL_PATH}" "${DISK_PATH}" "${TMPDIR}/vm_create.sh" --transform='s#.*/##'

rm -rf "${TMPDIR}"

