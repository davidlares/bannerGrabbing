# BannerGrabbing

This repo contains a simple Python script `bannergrabbing.py` which performs a socket connection (IPv4 - TCP) through a network segment looking for vulnerable service banners specified on a text file called `banners.txt`.

`BannerGrabbing` is a technique used to gain information about a computer system on a network and the services running on its open ports. It is used for `sysadmins` in order to take inventory of the systems and services on their network.

But intruders or "hackers" use `BannerGrabbing` techniques to know what's running on a specific network and see what can be vulnerable or not (mostly with known exploit possibilities).

## What it does

- Detect machines that run vulnerable services
- Loop through a list of ports defined on the `ports.txt`
- For each host on the network segment, it will create a connection to the remote host
- Will compare the service panel of the connection vs the known banner list that supposes to be vulnerable. Ex: `220 ProFTDP 1.3.1 Server (Debian)`

## Usage

`python bannergrabbing.py [network-segment]`

Something like:

`python bannergrabbing.py 192.168.1`

## Credits

 - [David E Lares](https://twitter.com/davidlares3)

## License

 - [MIT](https://opensource.org/licenses/MIT)
