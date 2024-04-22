cd $(git rev-parse --show-toplevel)

docker build --tag=backend --no-cache -f containers/Dockerfile.backend .