        .PHONY: run build logs down restart
        export DOCKER_BUILDKIT=1

        run: build
		docker compose up -d assistant-core

        build:
		docker compose build assistant-core

        logs:
		docker compose logs -f assistant-core

        down:
		docker compose down

        restart:
		make down && make run
