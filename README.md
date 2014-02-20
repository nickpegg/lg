# Looking Glass

This is a simple, not-very-cleverly-named looking glass tool. Supports pinging and MTRing arbitrary addresses. Doesn't support BGP tables like a lot of looking glass tools do since I don't personally own a router that speaks it with the internet.


## Docker Image
This repo is a Docker Trusted Build, so you can easily run your own Looking Glass tool with Docker!

Simply running `sudo docker run -d nickpegg/looking-glass` will get you a container running this app under uwsgi on port 5000, in an rbash environment restricted to only running `ping` and `mtr`.

You will need to configure a webserver to serve this app as well as the files under `/static/`.


## Caveats

I recommend running this as a non-privileged user stuck inside of rbash. I tried to keep people from injecting commands, but you can never be too cautious.

I also don't do any rate-limiting since whichever front-end webserver you choose (nginx, apache, etc.) is better suited to do that task.
