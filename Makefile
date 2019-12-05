clean:
	$(info =====  $@  =====)
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*.~' -exec rm -f {} +
	find . -name '.cache' -exec rm -rf {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name 'node_modules' -exec rm -rf {} +

build-test:
	pipenv install

run-test:
	pipenv run python src/test/e2e/solution.py

stop-app:
	docker stop ecsd-tech-test

full-run:
	@make stop-app
	./build.sh
	./run.sh
	@make run-test