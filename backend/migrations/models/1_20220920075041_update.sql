-- upgrade --
ALTER TABLE "event" ADD "user_id" UUID NOT NULL;
ALTER TABLE "event" ADD "category" VARCHAR(255) NOT NULL;
ALTER TABLE "event" ADD CONSTRAINT "fk_event_user_fd530cb5" FOREIGN KEY ("user_id") REFERENCES "user" ("uuid") ON DELETE CASCADE;
-- downgrade --
ALTER TABLE "event" DROP CONSTRAINT "fk_event_user_fd530cb5";
ALTER TABLE "event" DROP COLUMN "user_id";
ALTER TABLE "event" DROP COLUMN "category";
