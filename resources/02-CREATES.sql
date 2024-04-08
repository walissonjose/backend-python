create table if not exists calendar.users (
    user_cd_user uuid primary key,
    user_nm_user text not null,
    user_nm_mail text not null,
    CONSTRAINT user_nm_mail_unique UNIQUE (user_nm_mail)
);

comment on table calendar.users is 'Table containing all users of the system';
comment on column calendar.users.user_cd_user is 'Unique identifier of the user';
comment on column calendar.users.user_nm_user is 'Name of the user';
comment on column calendar.users.user_nm_mail is 'Email of the user';

create table if not exists calendar.rooms (
    room_cd_room uuid primary key,
    room_nm_room text not null,
    room_nr_capacity integer not null,
    constraint room_nm_capacity_positive check (room_nr_capacity > 0)
);

comment on table calendar.rooms is 'Table containing all rooms of the system';
comment on column calendar.rooms.room_cd_room is 'Unique identifier of the room';

create table if not exists calendar.meetings (
    meet_cd_meeting uuid primary key,
    meet_nm_title text not null,
    meet_df_start timestamp not null,
    meet_df_end timestamp not null,
    meet_dt_created date not null,
    room_cd_room uuid,
    constraint meet_df_start_end check (meet_df_start < meet_df_end),
    constraint room_cd_foreign_key foreign key (room_cd_room) references calendar.rooms (room_cd_room)
);

comment on table calendar.meetings is 'Table containing all meetings of the system';
comment on column calendar.meetings.meet_cd_meeting is 'Unique identifier of the meeting';
comment on column calendar.meetings.meet_nm_title is 'Title of the meeting';
comment on column calendar.meetings.meet_df_start is 'Start date and time of the meeting';
comment on column calendar.meetings.meet_df_end is 'End date and time of the meeting';
comment on column calendar.meetings.meet_dt_created is 'Date of the creation of the meeting';
comment on column calendar.meetings.room_cd_room is 'Room where the meeting will take place';

create table if not exists calendar.participants (
    meet_cd_meeting uuid not null,
    user_cd_participant uuid not null,
    primary key (meet_cd_meeting, user_cd_participant),
    foreign key (meet_cd_meeting) references calendar.meetings (meet_cd_meeting),
    foreign key (user_cd_participant) references calendar.users (user_cd_user)
);

comment on table calendar.participants is 'Table containing all participants of the meetings';
comment on column calendar.participants.meet_cd_meeting is 'Unique identifier of the meeting';
comment on column calendar.participants.user_cd_participant is 'Unique identifier of the participant';
