-- Inserts to populate table users
INSERT INTO calendar.users (user_cd_user, user_nm_user, user_nm_mail) VALUES ('11111111-1111-1111-1111-111111111111', 'João', 'joao@email.com');
INSERT INTO calendar.users (user_cd_user, user_nm_user, user_nm_mail) VALUES ('22222222-2222-2222-2222-222222222222', 'Maria', 'maria@email.com');
INSERT INTO calendar.users (user_cd_user, user_nm_user, user_nm_mail) VALUES ('33333333-3333-3333-3333-333333333333', 'Pedro', 'joao@email.com');

INSERT INTO calendar.users (user_cd_user, user_nm_mail) VALUES ('44444444-4444-4444-4444-444444444444', 'semnome@email.com');

-- Inserts to populate table meetings
INSERT INTO calendar.meetings (meet_cd_meeting, meet_nm_title, meet_df_start, meet_df_end, meet_dt_created) VALUES ('11111111-1111-1111-1111-111111111111', 'Reunião de Planejamento', '2024-04-08 09:00:00', '2024-04-08 10:30:00', '2024-04-08');
INSERT INTO calendar.meetings (meet_cd_meeting, meet_nm_title, meet_df_start, meet_df_end, meet_dt_created) VALUES ('22222222-2222-2222-2222-222222222222', 'Apresentação de Projeto', '2024-04-10 14:00:00', '2024-04-10 16:00:00', '2024-04-09');

INSERT INTO calendar.meetings (meet_cd_meeting, meet_nm_title, meet_df_start, meet_df_end, meet_dt_created) VALUES ('33333333-3333-3333-3333-333333333333', 'Reunião de Teste', '2024-04-12 15:00:00', '2024-04-12 14:00:00', '2024-04-11');

-- Inserts to populate table participants
INSERT INTO calendar.participants (meet_cd_meeting, user_cd_participant) VALUES ('11111111-1111-1111-1111-111111111111', '11111111-1111-1111-1111-111111111111');
INSERT INTO calendar.participants (meet_cd_meeting, user_cd_participant) VALUES ('22222222-2222-2222-2222-222222222222', '22222222-2222-2222-2222-222222222222');

INSERT INTO calendar.participants (meet_cd_meeting, user_cd_participant) VALUES ('99999999-9999-9999-9999-999999999999', '11111111-1111-1111-1111-111111111111');

-- Inserts to populate table rooms
INSERT INTO calendar.rooms (room_cd_room, room_nm_room, room_nr_capacity) VALUES ('11111111-1111-1111-1111-111111111111', 'Sala 1', 10);
INSERT INTO calendar.rooms (room_cd_room, room_nm_room, room_nr_capacity) VALUES ('22222222-2222-2222-2222-222222222222', 'Sala 2', 15);

INSERT INTO calendar.rooms (room_cd_room, room_nm_room, room_nr_capacity) VALUES ('33333333-3333-3333-3333-333333333333', 'Sala 3', -5);

-- Inserts to populate table reservations
INSERT INTO calendar.reservations (room_cd_reservated_room, meet_cd_meeting) VALUES ('11111111-1111-1111-1111-111111111111', '11111111-1111-1111-1111-111111111111');
INSERT INTO calendar.reservations (room_cd_reservated_room, meet_cd_meeting) VALUES ('22222222-2222-2222-2222-222222222222', '22222222-2222-2222-2222-222222222222');

INSERT INTO calendar.reservations (room_cd_reservated_room, meet_cd_meeting) VALUES ('99999999-9999-9999-9999-999999999999', '11111111-1111-1111-1111-111111111111');

