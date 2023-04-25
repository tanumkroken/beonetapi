docker run --rm \
  -v ${PWD}:/local openapitools/openapi-generator-cli generate \
  -i /local/openapi_beonet.yml \
  -g python \
  -o /local/beoremote \
  --package-name beoremote-cli