/* Det skal legges inn nødvendige data slik at systemet kan håndtere billettkjøp for de tre togrutene
på Nordlandsbanen, mandag 3. april og tirsdag 4. april i år. Dette kan gjøres med et skript, dere
trenger ikke å programmere støtte for denne funksjonaliteten */

/* Opprette togruteforekomster */
insert into Togruteforekomst(dato, rutenr)
values ("2023-03-04", "1");

insert into Togruteforekomst(dato, rutenr)
values ("2023-03-04", "2");

insert into Togruteforekomst(dato, rutenr)
values ("2023-03-04", "3");

insert into Togruteforekomst(dato, rutenr)
values ("2023-04-04", "1");

insert into Togruteforekomst(dato, rutenr)
values ("2023-04-04", "2");

insert into Togruteforekomst(dato, rutenr)
values ("2023-04-04", "3");


/* Opretter billetter til vogn 1 på rute 1 */
insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (1, 1, 1, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (2, 1, 1, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (3, 1, 1, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (4, 1, 1, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (5, 1, 1, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (6, 2, 1, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (7, 2, 1, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (8, 2, 1, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (9, 2, 1, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (10, 2, 1, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (11, 3, 1, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (12, 3, 1, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (13, 3, 1, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (14, 3, 1, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (15, 3, 1, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (16, 4, 1, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (17, 4, 1, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (18, 4, 1, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (19, 4, 1, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (20, 4, 1, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (21, 5, 1, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (22, 5, 1, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (23, 5, 1, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (24, 5, 1, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (25, 5, 1, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (26, 6, 1, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (27, 6, 1, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (28, 6, 1, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (29, 6, 1, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (30, 6, 1, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (31, 7, 1, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (32, 7, 1, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (33, 7, 1, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (34, 7, 1, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (35, 7, 1, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (36, 8, 1, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (37, 8, 1, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (38, 8, 1, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (39, 8, 1, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (40, 8, 1, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (41, 9, 1, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (42, 9, 1, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (43, 9, 1, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (44, 9, 1, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (45, 9, 1, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (46, 10, 1, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (47, 10, 1, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (48, 10, 1, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (49, 10, 1, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (50, 10, 1, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (51, 11, 1, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (52, 11, 1, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (53, 11, 1, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (54, 11, 1, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (55, 11, 1, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (56, 12, 1, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (57, 12, 1, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (58, 12, 1, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (59, 12, 1, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (60, 12, 1, "Fauske", "Bodø");




/* Oppretter billetter til vogn 2 på rute 1 */
insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (61, 1, 2, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (62, 1, 2, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (63, 1, 2, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (64, 1, 2, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (65, 1, 2, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (66, 2, 2, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (67, 2, 2, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (68, 2, 2, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (69, 2, 2, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (70, 2, 2, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (71, 3, 2, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (72, 3, 2, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (73, 3, 2, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (74, 3, 2, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (75, 3, 2, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (76, 4, 2, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (77, 4, 2, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (78, 4, 2, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (79, 4, 2, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (80, 4, 2, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (81, 5, 2, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (82, 5, 2, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (83, 5, 2, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (84, 5, 2, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (85, 5, 2, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (86, 6, 2, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (87, 6, 2, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (88, 6, 2, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (89, 6, 2, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (90, 6, 2, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (91, 7, 2, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (92, 7, 2, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (93, 7, 2, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (94, 7, 2, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (95, 7, 2, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (96, 8, 2, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (97, 8, 2, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (98, 8, 2, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (99, 8, 2, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (100, 8, 2, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (101, 9, 2, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (102, 9, 2, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (103, 9, 2, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (104, 9, 2, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (105, 9, 2, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (106, 10, 2, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (107, 10, 2, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (108, 10, 2, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (109, 10, 2, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (110, 10, 2, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (111, 11, 2, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (112, 11, 2, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (113, 11, 2, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (114, 11, 2, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (115, 11, 2, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (116, 12, 2, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (117, 12, 2, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (118, 12, 2, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (119, 12, 2, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (120, 12, 2, "Fauske", "Bodø");



/* Oppretter billetter for vogn 3 på rute 2 */
insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (121, 1, 3, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (122, 1, 3, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (123, 1, 3, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (124, 1, 3, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (125, 1, 3, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (126, 2, 3, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (127, 2, 3, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (128, 2, 3, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (129, 2, 3, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (130, 2, 3, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (131, 3, 3, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (132, 3, 3, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (133, 3, 3, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (134, 3, 3, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (135, 3, 3, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (136, 4, 3, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (137, 4, 3, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (138, 4, 3, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (139, 4, 3, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (140, 4, 3, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (141, 5, 3, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (142, 5, 3, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (143, 5, 3, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (144, 5, 3, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (145, 5, 3, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (146, 6, 3, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (147, 6, 3, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (148, 6, 3, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (149, 6, 3, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (150, 6, 3, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (151, 7, 3, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (152, 7, 3, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (153, 7, 3, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (154, 7, 3, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (155, 7, 3, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (156, 8, 3, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (157, 8, 3, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (158, 8, 3, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (159, 8, 3, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (160, 8, 3, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (161, 9, 3, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (162, 9, 3, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (163, 9, 3, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (164, 9, 3, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (165, 9, 3, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (166, 10, 3, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (167, 10, 3, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (168, 10, 3, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (169, 10, 3, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (170, 10, 3, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (171, 11, 3, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (172, 11, 3, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (173, 11, 3, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (174, 11, 3, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (175, 11, 3, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (176, 12, 3, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (177, 12, 3, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (178, 12, 3, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (179, 12, 3, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (180, 12, 3, "Fauske", "Bodø");



/* Oppretter biletter for vogn 4 på rute 2 */
insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (181, 1, 4, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (182, 1, 4, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (183, 1, 4, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (184, 1, 4, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (185, 1, 4, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (186, 2, 4, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (187, 2, 4, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (188, 2, 4, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (189, 2, 4, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (190, 2, 4, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (191, 3, 4, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (192, 3, 4, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (193, 3, 4, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (194, 3, 4, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (195, 3, 4, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (196, 4, 4, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (197, 4, 4, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (198, 4, 4, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (199, 4, 4, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (200, 4, 4, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (201, 5, 4, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (202, 5, 4, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (203, 5, 4, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (204, 5, 4, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (205, 5, 4, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (206, 6, 4, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (207, 6, 4, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (208, 6, 4, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (209, 6, 4, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (210, 6, 4, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (211, 7, 4, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (212, 7, 4, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (213, 7, 4, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (214, 7, 4, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (215, 7, 4, "Fauske", "Bodø");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (216, 8, 4, "Trondheim S", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (217, 8, 4, "Steinkjer", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (218, 8, 4, "Mosjøen", "Mo I Rana");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (219, 8, 4, "Mo I Rana", "Fauske");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (220, 8, 4, "Fauske", "Bodø");



/* Oppretter billetter for vogn 5 på rute 3 */
insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (221, 1, 5, "Mo I Rana", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (222, 1, 5, "Mosjøen", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (223, 1, 5, "Steinkjer", "Trondheim S");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (224, 2, 5, "Mo I Rana", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (225, 2, 5, "Mosjøen", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (226, 2, 5, "Steinkjer", "Trondheim S");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (227, 3, 5, "Mo I Rana", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (228, 3, 5, "Mosjøen", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (229, 3, 5, "Steinkjer", "Trondheim S");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (230, 4, 5, "Mo I Rana", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (231, 4, 5, "Mosjøen", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (232, 4, 5, "Steinkjer", "Trondheim S");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (233, 5, 5, "Mo I Rana", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (234, 5, 5, "Mosjøen", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (235, 5, 5, "Steinkjer", "Trondheim S");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (236, 6, 5, "Mo I Rana", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (237, 6, 5, "Mosjøen", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (238, 6, 5, "Steinkjer", "Trondheim S");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (239, 7, 5, "Mo I Rana", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (240, 7, 5, "Mosjøen", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (241, 7, 5, "Steinkjer", "Trondheim S");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (242, 8, 5, "Mo I Rana", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (243, 8, 5, "Mosjøen", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (244, 8, 5, "Steinkjer", "Trondheim S");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (245, 9, 5, "Mo I Rana", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (246, 9, 5, "Mosjøen", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (247, 9, 5, "Steinkjer", "Trondheim S");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (248, 10, 5, "Mo I Rana", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (249, 10, 5, "Mosjøen", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (250, 10, 5, "Steinkjer", "Trondheim S");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (251, 11, 5, "Mo I Rana", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (252, 11, 5, "Mosjøen", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (253, 11, 5, "Steinkjer", "Trondheim S");


insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (254, 12, 5, "Mo I Rana", "Mosjøen");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (255, 12, 5, "Mosjøen", "Steinkjer");

insert into Billett(billettnr, plassnr, vognID, startstasjon, endestasjon)
values (256, 12, 5, "Steinkjer", "Trondheim S");