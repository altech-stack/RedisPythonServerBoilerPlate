# Redis Python Server Boiler Plate

This project is a beginner's project to get you started with redis and flask. For a tutorial on how to use this, visit: https://www.andrewlien.com/random-bits-of-code/2017/10/24/multiprocessing-101



### Prerequisites

What things you need to install the software and how to install them

```
pip install requests flask redis rq
```


## Deployment

To create redis docker:

```
sudo docker run --name redis -d --restart=always -p 6379:6379 --volume /srv/docker/redis:/var/lib/redis sameersbn/redis:latest

```
To run flask server:

```
python multi_processing_server.py
```

To run the client:
```
python multi_processing_client.py
``` 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* My workplace Exabeam (and my manager!) for improving my python knowledge
