-- Inserts to populate table users
INSERT INTO calendar.users (user_cd_user, user_nm_user, user_nm_mail)
VALUES ('11111111-1111-1111-1111-111111111111', 'Tiago Lobo', 'tiago@email.com');
INSERT INTO calendar.users (user_cd_user, user_nm_user, user_nm_mail)
VALUES ('22222222-2222-2222-2222-222222222222', 'Gabriel Freitas', 'gabriel@email.com');
INSERT INTO calendar.users (user_cd_user, user_nm_user, user_nm_mail)
VALUES ('33333333-3333-3333-3333-333333333333', 'Daniel Borges', 'daniel@email.com');
INSERT INTO calendar.users (user_cd_user, user_nm_user, user_nm_mail)
VALUES ('44444444-4444-4444-4444-444444444444', 'João', 'joao@email.com');
INSERT INTO calendar.users (user_cd_user, user_nm_user, user_nm_mail)
VALUES ('55555555-5555-5555-5555-555555555555', 'Maria', 'maria@email.com');
INSERT INTO calendar.users (user_cd_user, user_nm_user, user_nm_mail)
VALUES ('66666666-6666-6666-6666-666666666666', 'Pedro', 'pedro@email.com');
INSERT INTO calendar.users (user_cd_user, user_nm_user, user_nm_mail)
VALUES ('77777777-7777-7777-7777-777777777777', 'Ana', 'ana@email.com');
INSERT INTO calendar.users (user_cd_user, user_nm_user, user_nm_mail)
VALUES ('88888888-8888-8888-8888-888888888888', 'Laura', 'laura@email.com');
INSERT INTO calendar.users (user_cd_user, user_nm_user, user_nm_mail)
VALUES ('99999999-9999-9999-9999-999999999999', 'Lucas', 'lucas@email.com');
INSERT INTO calendar.users (user_cd_user, user_nm_user, user_nm_mail)
VALUES ('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', 'Mariana', 'mariana@email.com');

-- Inserts to populate table rooms
INSERT INTO calendar.rooms (room_cd_room, room_nm_room, room_nr_capacity)
VALUES ('11111111-1111-1111-1111-111111111111', 'Sala de Reunião 1', 10);
INSERT INTO calendar.rooms (room_cd_room, room_nm_room, room_nr_capacity)
VALUES ('22222222-2222-2222-2222-222222222222', 'Sala de Treinamento', 20);
INSERT INTO calendar.rooms (room_cd_room, room_nm_room, room_nr_capacity)
VALUES ('33333333-3333-3333-3333-333333333333', 'Auditório Principal', 100);
INSERT INTO calendar.rooms (room_cd_room, room_nm_room, room_nr_capacity)
VALUES ('44444444-4444-4444-4444-444444444444', 'Sala de Entrevistas', 5);
INSERT INTO calendar.rooms (room_cd_room, room_nm_room, room_nr_capacity)
VALUES ('55555555-5555-5555-5555-555555555555', 'Sala de Conferências', 50);
INSERT INTO calendar.rooms (room_cd_room, room_nm_room, room_nr_capacity)
VALUES ('66666666-6666-6666-6666-666666666666', 'Sala de Videoconferência', 15);
INSERT INTO calendar.rooms (room_cd_room, room_nm_room, room_nr_capacity)
VALUES ('77777777-7777-7777-7777-777777777777', 'Sala de Reunião Executiva', 8);
INSERT INTO calendar.rooms (room_cd_room, room_nm_room, room_nr_capacity)
VALUES ('88888888-8888-8888-8888-888888888888', 'Sala de Criatividade', 12);
INSERT INTO calendar.rooms (room_cd_room, room_nm_room, room_nr_capacity)
VALUES ('99999999-9999-9999-9999-999999999999', 'Sala de Conferências 2', 60);
INSERT INTO calendar.rooms (room_cd_room, room_nm_room, room_nr_capacity)
VALUES ('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', 'Sala de Conferências 3', 70);

-- Inserts to populate table meetings

-- Reunião 1: Sala de Reunião 1
INSERT INTO calendar.meetings (meet_cd_meeting, meet_nm_title, meet_df_start, meet_df_end, meet_dt_created,
                               room_cd_room)
VALUES ('11111111-1111-1111-1111-111111111111', 'Brainstorming de Projeto', '2024-04-08 10:00:00',
        '2024-04-08 12:00:00', '2024-04-07', '11111111-1111-1111-1111-111111111111');

-- Participantes: Tiago Lobo, Gabriel Freitas
INSERT INTO calendar.participants (meet_cd_meeting, user_cd_participant)
VALUES ('11111111-1111-1111-1111-111111111111', '11111111-1111-1111-1111-111111111111'),
       ('11111111-1111-1111-1111-111111111111', '22222222-2222-2222-2222-222222222222');

-- Reunião 2: Sala de Treinamento
INSERT INTO calendar.meetings (meet_cd_meeting, meet_nm_title, meet_df_start, meet_df_end, meet_dt_created,
                               room_cd_room)
VALUES ('22222222-2222-2222-2222-222222222222', 'Apresentação de Produto', '2024-04-09 14:00:00', '2024-04-09 16:00:00',
        '2024-04-07', '22222222-2222-2222-2222-222222222222');

-- Participantes: Daniel Borges, Maria
INSERT INTO calendar.participants (meet_cd_meeting, user_cd_participant)
VALUES ('22222222-2222-2222-2222-222222222222', '33333333-3333-3333-3333-333333333333'),
       ('22222222-2222-2222-2222-222222222222', '55555555-5555-5555-5555-555555555555');

-- Reunião 3: Auditório Principal
INSERT INTO calendar.meetings (meet_cd_meeting, meet_nm_title, meet_df_start, meet_df_end, meet_dt_created,
                               room_cd_room)
VALUES ('33333333-3333-3333-3333-333333333333', 'Sessão de Abertura', '2024-04-10 09:00:00', '2024-04-10 10:30:00',
        '2024-04-07', '33333333-3333-3333-3333-333333333333');

-- Participantes: João, Ana, Laura
INSERT INTO calendar.participants (meet_cd_meeting, user_cd_participant)
VALUES ('33333333-3333-3333-3333-333333333333', '44444444-4444-4444-4444-444444444444'),
       ('33333333-3333-3333-3333-333333333333', '77777777-7777-7777-7777-777777777777'),
       ('33333333-3333-3333-3333-333333333333', '88888888-8888-8888-8888-888888888888');

-- Reunião 4: Sala de Entrevistas
INSERT INTO calendar.meetings (meet_cd_meeting, meet_nm_title, meet_df_start, meet_df_end, meet_dt_created,
                               room_cd_room)
VALUES ('44444444-4444-4444-4444-444444444444', 'Entrevistas de Emprego', '2024-04-11 10:00:00', '2024-04-11 12:00:00',
        '2024-04-07', '44444444-4444-4444-4444-444444444444');


