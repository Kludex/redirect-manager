.PHONY: install
install:
	@echo "🔨 Installing dependencies"
	pip install -r requirements.txt
	pip install -r dev-requirements.txt

.PHONY: tests
tests:
	@echo "✅ Running tests"
	pytest

.PHONY: create_env
create_env:
	@echo "⚡️ Create environment"
	cp env-sample .env
