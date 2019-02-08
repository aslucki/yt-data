IMAGE_NAME=yt_data

build_image:
	docker build -t $(IMAGE_NAME) .

dev:
	docker run --rm -ti \
		-v $(PWD)/:/project \
		-w="/project" \
		$(IMAGE_NAME)

test:
	python3 -m pytest tests/