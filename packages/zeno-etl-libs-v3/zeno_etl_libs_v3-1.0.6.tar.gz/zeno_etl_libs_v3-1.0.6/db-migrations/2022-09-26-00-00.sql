ALTER TABLE "prod2-generico"."bills-1-metadata" ADD "total-cashback" NUMERIC(10,2) NULL  ENCODE az64;
ALTER TABLE "prod2-generico"."bills-1-metadata" ADD "zenocare-amount" NUMERIC(10,2) NULL  ENCODE az64;
ALTER TABLE "prod2-generico"."bills-1-metadata" ADD "is-generic-chronic" BOOLEAN   ENCODE RAW;
ALTER TABLE "prod2-generico"."retention-master"  ADD "total-cashback" NUMERIC(10,2) NULL  ENCODE az64;
ALTER TABLE "prod2-generico"."retention-master"  ADD "zenocare-amount" NUMERIC(10,2) NULL  ENCODE az64;