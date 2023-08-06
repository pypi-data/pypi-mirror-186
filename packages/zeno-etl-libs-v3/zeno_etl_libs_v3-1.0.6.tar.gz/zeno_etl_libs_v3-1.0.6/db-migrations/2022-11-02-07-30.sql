CREATE TABLE IF NOT EXISTS "prod2-generico"."lat-long-nearest-store"
(
	"created-at" TIMESTAMP WITHOUT TIME ZONE   ENCODE az64
	,latitude VARCHAR(765)   ENCODE lzo
	,longitude VARCHAR(765)   ENCODE lzo
	,"nearest-store-id" INTEGER NOT NULL  ENCODE az64
)
DISTSTYLE AUTO;