check_install_xvfb() {
    if hash xvfb-run 2>/dev/null; then
        :
    else
        sudo apt-get update
		sudo apt-get upgrade
		sudo apt-get install xvfb
    fi
}
check_install_xvfb
export DISPLAY=localhost:1.0
xvfb-run -a bash .misc/tests.sh
