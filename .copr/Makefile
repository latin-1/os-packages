.PHONY: srpm

srpm:
	dnf install fedpkg --assumeyes
	./build-srpm.sh "$(outdir)"
