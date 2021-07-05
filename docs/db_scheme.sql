CREATE TABLE "User" (
  "id" int PRIMARY KEY,
  "username" varchar UNIQUE,
  "first_name" varchar,
  "last_name" int,
  "email" varchar,
  "groups" text,
  "last_login" date,
  "first_joined" date,
  "birth_date" date,
  "auth_source" enum
);

CREATE TABLE "SmokerSupporter" (
  "id" int PRIMARY KEY,
  "smokerid" int,
  "supporterid" int,
  "date_linked" date,
  "is_active" boolean,
  "relationship" enum
);

CREATE TABLE "UserConnection" (
  "id" int PRIMARY KEY,
  "smokerid" int,
  "supporter_username" int,
  "verification_code" varchar,
  "supporter_email" varchar
);

CREATE TABLE "SmokeConfig" (
  "id" int PRIMARY KEY,
  "userid" int,
  "frequency" enum,
  "cost_per_pack" double,
  "currency" enum,
  "smoking_type" enum,
  "brand" enum,
  "quit_date" date,
  "years_smoked" int
);

CREATE TABLE "NotifConfig" (
  "id" int PRIMARY KEY,
  "smokersupporterid" int,
  "smokeconfigid" int,
  "notif_type" enum,
  "time" time
);

CREATE TABLE "NotifDay" (
  "id" int PRIMARY KEY,
  "notifconfigid" int,
  "day" enum
);

CREATE TABLE "NotifLaunch" (
  "id" int PRIMARY KEY,
  "userid" int,
  "content" text,
  "launch_date" datetime,
  "notif_type" enum
);

CREATE TABLE "SmokeEntry" (
  "id" int PRIMARY KEY,
  "smokeconfigid" int,
  "smoked" int,
  "cravings" int,
  "intensity" enum,
  "date" datetime,
  "date_filled" datetime
);

ALTER TABLE "SmokerSupporter" ADD FOREIGN KEY ("smokerid") REFERENCES "User" ("id");

ALTER TABLE "SmokerSupporter" ADD FOREIGN KEY ("supporterid") REFERENCES "User" ("id");

ALTER TABLE "UserConnection" ADD FOREIGN KEY ("smokerid") REFERENCES "User" ("id");

ALTER TABLE "UserConnection" ADD FOREIGN KEY ("supporter_username") REFERENCES "User" ("username");

ALTER TABLE "SmokeConfig" ADD FOREIGN KEY ("userid") REFERENCES "User" ("id");

ALTER TABLE "NotifConfig" ADD FOREIGN KEY ("smokersupporterid") REFERENCES "SmokerSupporter" ("id");

ALTER TABLE "NotifConfig" ADD FOREIGN KEY ("smokeconfigid") REFERENCES "SmokeConfig" ("id");

ALTER TABLE "NotifDay" ADD FOREIGN KEY ("notifconfigid") REFERENCES "NotifConfig" ("id");

ALTER TABLE "NotifLaunch" ADD FOREIGN KEY ("userid") REFERENCES "User" ("id");

ALTER TABLE "SmokeEntry" ADD FOREIGN KEY ("smokeconfigid") REFERENCES "SmokeConfig" ("id");
