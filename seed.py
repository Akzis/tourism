from main import db, Place, PlaceImage, Country, Like, Region, RegionPlace, RegionPlaceImage

try:
    db.drop_tables([Place, PlaceImage, Country, Like, Region, RegionPlace, RegionPlaceImage])
    db.create_tables([Place, PlaceImage, Country, Like, Region, RegionPlace, RegionPlaceImage])
except:
    print("Error")
    pass

country1 = Country.create(
    name="Швеция",
    description="Швеция – это государство в Скандинавии, география которого включает тысячи прибрежных островов и внутриматериковых озер, таежные леса и горы, покрытые ледниками.",
    image="https://a.storyblok.com/f/176292/5616x3744/a8357d5a7f/sweden-citizenship-102698667.jpeg",
    side_of_the_world="Europe",
)

country2 = Country.create(
    name="Норвегия",
    description="Норвегия - вытянутая и узкая страна, более 30% территории которой покрыто лесами, множеством рек и озёр. Более половины площади страны занято горными массивами. Численность населения Норвегии - около 4,3 миллионов человек.",
    image="https://cdn.tripster.ru/thumbs2/ad74c10e-c3af-11ee-aaf6-f6eac2c3b054.1220x600.jpeg",
    side_of_the_world="Europe",
)

country3 = Country.create(
    name="Япония",
    description="	Япония — островное государство в Восточной Азии, расположенное на большом архипелаге, который входит в систему Тихоокеанского вулканического огненного кольца. Японские острова омываются водами Тихого океана.",
    image="https://www.state.gov/wp-content/uploads/2023/04/shutterstock_667925704-scaled-e1681732163864.jpg",
    side_of_the_world="Asia",
)

country4 = Country.create(
    name="Бразилия",
    description="Бразилия — крупнейшая страна Южной Америки и Латинской Америки как по территории, так и по численности населения.Занимает центральную и восточную часть материка Южная Америка.",
    image="https://www.baltma.ru/upload/iblock/84c/84cc203c26735cd5c4dab45699fc0050.jpg",
    side_of_the_world="South America",
)

country5 = Country.create(
    name="Канада",
    description="Канада — государство в Северной Америке, крупнейшее по площади на этом континенте и второе по площади в мире. По численности населения 37-е государство в мире (более 41 млн жителей в марте 2024 года).",
    image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDQGUswF0AkdHxS8rvP6BqoezB0rEl23SrIQ&s",
    side_of_the_world="North America",
)

country6 = Country.create(
    name="Австралия",
    description="Австралия — государство в Южном полушарии, расположенное на одноимённом материке, а также близлежащих островах Тихого и Индийского океанов. Официальное название страны — Австралийский союз.",
    image="https://static.tildacdn.com/tild3764-3239-4461-b561-303261343939/image001.jpg",
    side_of_the_world="Australia and Oceania",
)

country7 = Country.create(
    name="Египет",
    description="Египет — трансконтинентальное государство, расположенное в Северной Африке и на Ближнем Востоке (Синайский полуостров). На северо-востоке граничит с Израилем и частично признанным государством Палестиной.",
    image="https://naked-science.ru/wp-content/uploads/2023/11/kmplksgiza.jpg",
    side_of_the_world="Africa",
)

country8 = Country.create(
    name="Финляндия",
    description="Финляндия — государство в Северной Европе на восточном берегу Балтийского моря. Граничит со Швецией на западе, Россией на востоке и Норвегией на севере.",
    image="https://iworld.com/wp-content/uploads/2023/03/life-finland-900x467.jpg",
    side_of_the_world="Europe",
)

country9 = Country.create(
    name="Великобритания",
    description="Великобритания — государство в Европе, расположенное на острове Великобритания, северо-восточной части острова Ирландия и нескольких более мелких островах.",
    image="https://i.pinimg.com/originals/7a/e3/f7/7ae3f728f2546df6bce633918e123a36.jpg",
    side_of_the_world="Europe",
)

country10 = Country.create(
    name="Южная Корея",
    description="Южная Корея — государство в Восточной Азии, расположенное в южной части Корейского полуострова. Площадь страны составляет 100 449 км², население, по оценке 2023 года — более 51 миллиона человек. Столица и крупнейший город — Сеул.",
    image="https://avatars.mds.yandex.net/i?id=2d522e409e94b6d6119d966d55078a06_l-4216502-images-thumbs&n=13",
    side_of_the_world="Asia",
)


# начало --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


country12 = Country.create(
    name="Китай",
    description="Китай — крупнейшее государство Восточной Азии, с богатой историей, крупнейшей численностью населения и второй экономикой мира.",
    image="https://www.chengduprivatetour.com/upload/ueditor/image/20190226/6368679340742187503907761.jpg",
    side_of_the_world="Asia",
)

country13 = Country.create(
    name="Франция",
    description="Франция — страна в Западной Европе, известная своей культурой, кухней и достопримечательностями, включая Эйфелеву башню и Лувр.",
    image="https://s1.1zoom.ru/big3/487/Sky_Evening_France_Eiffel_Tower_Paris_From_above_520603_5416x3611.jpg",
    side_of_the_world="Europe",
)

country14 = Country.create(
    name="Германия",
    description="Германия — страна в Центральной Европе, экономический и технологический лидер Европейского союза.",
    image="https://taxi-aeroport-minsk2.by/wp-content/uploads/2022/06/cologne_1.jpeg",
    side_of_the_world="Europe",
)

country15 = Country.create(
    name="Аргентина",
    description="Аргентина — вторая по величине страна Южной Америки, известная танго, футболом и природными контрастами.",
    image="https://news.delta.com/sites/default/files/2024-10/buenosaires.jpg",
    side_of_the_world="South America",
)

country16 = Country.create(
    name="Мексика",
    description="Мексика — страна в Северной Америке, с богатой историей майя и ацтеков, а также знаменитыми пляжами и кухней.",
    image="https://img.nh-hotels.net/8yYbq/XJ0B8/original/Mexico_Mexico_City_Zocalo_1.jpg?output-quality=70&resize=*:*&background-color=white",
    side_of_the_world="North America",
)

country17 = Country.create(
    name="Италия",
    description="Италия — страна в Южной Европе, известная Древним Римом, архитектурой, искусством и кухней.",
    image="https://avatars.mds.yandex.net/i?id=ee138542eec0a59bfee599d1749a52a91632017d-5319522-images-thumbs&n=13",
    side_of_the_world="Europe",
)


country20 = Country.create(
    name="Новая Зеландия",
    description="Новая Зеландия — островное государство в юго-западной части Тихого океана, знаменитое своими пейзажами и экологией.",
    image="https://e3.365dm.com/20/11/2048x1152/skynews-new-zealand-milford-sound_5175937.jpg?20201118101902",
    side_of_the_world="Australia and Oceania",
)


country21 = Country.create(
    name="Испания",
    description="Испания — популярная туристическая страна в Южной Европе, славящаяся пляжами Коста-Брава, архитектурой Гауди в Барселоне и историческими памятниками Мадрида.",
    image="https://yandex-images.clstorage.net/RmqM53130/67c0e0jVIz/hOD47YPuVxNHoZFfJN8PLRAqys5uMzl3tV5pjGB3gDbIXOtzJG0XlMg3lEhBT4j8Q9rnkxddqm3f-p5SGsNPMMq2v6HEqUxOFeqPCyzcCi8Nd4nfcmk9Kq8cNdAhL9Ztz1yDHQcUZqm2Vb85PWCSqxSMsd1aSr4E4ruxN0LTPiSj0uHKhu8xCEi30GUz6xs_OULU50BWFju7QCTvAU7WIJs8kS4KIWGFlVKvFCR9rYI2sq7RIkmpIfTTqzFmxhY1m_fI4IjrECRCvdJnEeIECSJRx-5icDQAl2se9wRO1j-RLLopDiBHnKBSgz0yYrytEo-V1z1vvizy0J8jR-0rKqL03_6DyRcySbrFdCbFCSAdbNbvSl0CHbBjNtQ2dfkYmievJTIbYJ2MbpAIOkCPpTWwnsIkSoE81c6lFkn2Dz-bwOfJidIxN2W683EK1CAqIEXF20NRNSKQXwDIA2DtIrUNvyUeNm2ArlWkHwNGiaw3v4TGEECCFdroujFC7Q43uuPa9YfeMwZvntNFPcczKwxQ7f5jSAQYnnggxARn1imQBZ8rEgZ8hYF0nwQzSai9LqWF1BNPgi_r76okQsQpB6vK68i60B0zQLb4SQH5DQIbV8fdS0s-PJ9iIfoiUe8JlzyoCw0DY5uTVKELDUOJvSCBmMcNXI8hxeiLFmzICCaexuX5gf4zP2Gh1Vcz8AwsHVTD7UhaNCemVhf_MEDwKrAEvw8tO0GmjHWSNyFsnJ0Oj6XtLX6nLvzpty178B8zmvDY5rLZNhxvufZuFcAHIQJo_sdVdBIfr0oB1j9Z9BezP7QNKwZ0nZhDsQQef4OIC5uMyTtRviLX36o2S9oECJrs-ua91j4JapnIXBfnKCYAUcfJW04dCpBpAdYwYdA8vBylOBEiR7C9a74fN1SggRORs_EOS6wM1-GPFFjqLBq36fbtsNY-Fm2k-U4U5RgHPk7p31tuMxKfajz6OGI",
    side_of_the_world="Europe",
)

country22 = Country.create(
    name="Греция",
    description="Греция — страна в Юго-Восточной Европе, известная своими островами (Санторини, Миконос), античными руинами в Афинах и великолепной кухней.",
    image="https://www.mustgo.com/wp-content/uploads/2018/04/Santorini.jpg",
    side_of_the_world="Europe",
)

country23 = Country.create(
    name="Таиланд",
    description="Таиланд — популярное направление в Юго-Восточной Азии, привлекающее туристов храмами Бангкока, островами Пхукет и Краби, а также рынками на воде.",
    image="https://avatars.mds.yandex.net/i?id=a3fd9bc530ac1330909b077b743ce5611dbea697-5483535-images-thumbs&n=13",
    side_of_the_world="Asia",
)

country24 = Country.create(
    name="Швейцария",
    description="Швейцария — живописная страна в Центральной Европе, известная Альпами, озёрами Цюрих и Женевским, зимними курортами и шоколадом.",
    image="https://otvet.imgsmail.ru/download/u_a1a06027c353c2b4ab0234b61113adc7.jpg",
    side_of_the_world="Europe",
)

country25 = Country.create(
    name="Турция",
    description="Турция — трансконтинентальная страна между Европой и Азией, популярная историческими достопримечательностями Стамбула, курортами Анталии и каппадокийскими пейзажами.",
    image="https://avatars.mds.yandex.net/i?id=b3f0ab5e9b11efd99cd46cd2688623bdb69eabd2-5256069-images-thumbs&n=13",
    side_of_the_world="Asia/Europe",
)


# конец --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

place1 = Place.create(
    latitude=59.316242,
    longitude=18.102318,
    name="Озеро Меларен",
    description="Известно, что Стокгольм располагается на берегах Балтики. Но это не единственный водоем природного происхождения поблизости. Населенный пункт омывает еще озеро Меларен. В рейтинге самых больших по стране оно находится на третьем месте. Длина достигает 120 км, а ширина 64 км. Со всех сторон озеро окружено множеством островов, этим объясняется обилие достопримечательностей поблизости в виде древних замков, дворцов, усадеб, особняков. Всегда озеро привлекало туристов своей таинственностью, загадочностью.",
    country_id=country1.id,
)

place2 = Place.create(
    latitude=58.446174,
    longitude=14.884029,
    name="Вадстенский замок",
    description="Начать знакомство стоит с впечатляющего напоминания о славной истории государства. На его территории описываемая крепость является одной из самых старинных, ведь строить ее начали еще в 1545 году. Далеко не всем туристам известно, что изначально Вадстенский замок имел 4 круглых башни, 3 жилых здания из камня, несколько хозяйственных построек. В определенный момент необходимость в фортификационных сооружениях отпала, поэтому они были скрыты. Решение превратить постройку в исторический памятник было принято в XX веке, для чего были проведены масштабные реставрационные работы.",
    country_id=country1.id,
)

place3 = Place.create(
    latitude=61.669737,
    longitude=6.967598,
    name="Юстедальсбреен",
    description="Представляет собой самый большой на всей территории Европы ледник. Он имеет вид плато с 26-ю ледяными языками, отходящими в разные стороны. Общая площадь этой достопримечательности Норвегии составляет 1600 км². От нее берут свое начало и другие, не менее известные ледники. Территория, которую занимает ледник, включает в себя несколько муниципалитетов. Чуть больше 25 лет назад здесь основан парк национальной значимости.",
    country_id=country2.id,
)


place4 = Place.create( 
    latitude=62.098069,
    longitude=7.075320,
    name="Гейрангер-фьорд",
    description="Вряд ли вы останетесь равнодушными, если своими глазами увидите это творение природы. Речь идет о небольшом, но с великолепным ландшафтом, фьорде. Его длина составляет 20 км, однако это не мешает ему быть самым посещаемым. Оценивая все достопримечательности Норвегии, бывалые туристы на первое место ставят именно глубоководный изумрудный морской залив со скалистыми берегами. Если ваша душа жаждет развлечений, можно половить рыбу, покататься на байдарке, опробовать рафтинг. Здесь также предлагаются поездки верхом и даже в летнее время можно покататься на лыжах.",
    country_id=country2.id,
)

place5 = Place.create( 
    latitude=60.317419,
    longitude=6.190174,
    name="Стейнсдальсфосс",
    description="Этот водопад относится к числу самых фотографируемых. Его высота составляет 50 м, он является частью реки Фосселва. Под стремительно падающим с возвышенности потоком воды проходит пешеходная дорожка, в чем и заключается уникальность этой достопримечательности Норвегии. Таинственная, а где-то даже сказочная атмосфера создается за счет подсветки вертикального водоема прожекторами.",
    country_id=country2.id,
)

place6 = Place.create( 
    latitude=58.158244,
    longitude=8.706641,
    name="Дорога троллей",
    description="Норвежские городки Ондалснес и Валлдал соединяет дорога RV63, ее участок в долине Румсдален стабильно входит в первую десятку самых опасных автомобильных трасс мира. Кажется, что не люди, а тролли, горные духи, соорудили этот серпантин с 11 поворотами, карабкающийся по крутому склону и отделенный от 200-метровой пропасти только стоящими вдоль обочины столбиками из камней. Но Тролльстиген, он же Дорога троллей, — результат не колдовства, а труда норвежских рабочих, воплотивших в жизнь этот шедевр инженерного искусства.",
    country_id=country2.id,
)











place7 = Place.create( 
    latitude=66.543569,
    longitude=25.849022,
    name="Деревня Санта-Клауса",
    description="Деревня Санта-Клауса (фин. Joulupukin Pajakylä) — парк развлечений в Финляндии, посвящённый Рождественскому Деду, которого в Финляндии называют Йоулупукки, а в англоязычных странах — Санта-Клаус.",
    country_id=country8.id,
)

place8 = Place.create( 
    latitude=51.5228751,
    longitude=0.1549564,
    name="Музей мадам Тюссо",
    description="Музей мадам Тюссо — музей восковых фигур в лондонском районе Марилебон, созданный в 1835 году скульптором Марией Тюссо. ",
    country_id=country9.id,
)

place9 = Place.create( 
    latitude=37.575926,
    longitude=126.976794,
    name="Кёнбоккун",
    description="Кёнбоккун — дворцовый комплекс, расположенный на севере Сеула, Южная Корея. Был главным и крупнейшим дворцом династии Чосон, в котором жила королевская семья.",
    country_id=country10.id,
)

place10 = Place.create( 
    latitude=35.3624992,
    longitude=138.7305603,
    name="Гора Фудзияма",
    description="Фудзияма — действующий стратовулкан на японском острове Хонсю в 90 километрах к юго-западу от Токио. Высота вулкана — 3776 метров (пик Кенгамине, самая высокая точка в Японии).",
    country_id=country3.id,
)




place11 = Place.create(
    latitude=40.43205466898241,
    longitude=116.57037489739056,
    name="Великая Китайская стена",
    description="Великая Китайская стена — крепостная стена в Северном Китае, крупнейшее оборонительное сооружение в мире.",
    country_id=country12.id,
)


place12 = Place.create( 
    latitude=35.03954565884377,
    longitude=135.7292001818455,
    name="Кинкаку-дзи",
    description="Исторический храм с позолоченным фасадом среди живописных садов у зеркального озера.",
    country_id=country3.id,
)


place13 = Place.create( 
    latitude=35.63303589296367,
    longitude=139.88042648371976,
    name="Токийский парк",
    description="Токийский парк развлечений знаменитой франшизы, известный аттракционами, шоу и костюмированными персонажами.",
    country_id=country3.id,
)

PlaceImage.create(
    url="https://res.klook.com/image/upload/fl_lossy.progressive,q_85/c_fill,w_1000/v1712831385/fcctgo6yfehhghg1dg3c.jpg",
    place_id=place13.id,
)


PlaceImage.create(
    url="https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_6700d05e1fa4e5602c61b2a8_6700d134d4064b46fba1dcf6/scale_1200",
    place_id=place13.id,
)


PlaceImage.create(
    url="https://res.klook.com/image/upload/fl_lossy.progressive,q_85/c_fill,w_1000/v1712831385/fcctgo6yfehhghg1dg3c.jpg",
    place_id=place13.id,
)

PlaceImage.create(
    url="https://i.pinimg.com/736x/ff/17/c1/ff17c1d801358d171b1ced983e22c9f0.jpg",
    place_id=place12.id,
)


PlaceImage.create(
    url="https://i.pinimg.com/originals/65/65/e0/6565e029e39310c01949c41d6af6099c.jpg",
    place_id=place12.id,
)

PlaceImage.create(
    url="https://i.pinimg.com/originals/fb/d5/85/fbd585f3b37863b8dc0cfb3b503fb9a4.jpg",
    place_id=place11.id,
)



PlaceImage.create(
    url="https://avatars.mds.yandex.net/i?id=1c01486d4b60ba6273e99376bab83a4e917c8292-10639710-images-thumbs&n=13",
    place_id=place7.id,
)

PlaceImage.create(
    url="https://avatars.mds.yandex.net/i?id=d322f71f107f78efee9265e40c1139e82edc8cd8-10840543-images-thumbs&n=13",
    place_id=place7.id,
)

PlaceImage.create(
    url="https://i0.wp.com/ozernyi-sochi.ru/wp-content/uploads/c/d/7/cd7a6caebeded89fb4eb81b425e5428f.jpeg?ssl=1",
    place_id=place8.id,
)

PlaceImage.create(
    url="https://avatars.mds.yandex.net/i?id=3460c8791caaff2b444c8fdc36404d10db06022d-9041932-images-thumbs&n=13",
    place_id=place8.id,
)

PlaceImage.create(
    url="https://pp.userapi.com/c637124/v637124327/49909/GEgmjYCJkr0.jpg",
    place_id=place9.id,
)

PlaceImage.create(
    url="https://avatars.mds.yandex.net/i?id=e3893bb9f18c8d9db88a855efc17caf2_l-4593205-images-thumbs&n=13",
    place_id=place9.id,
)

PlaceImage.create(
    url="https://wallpapers.com/images/hd/colored-flowers-and-mount-fuji-o1psszzc4j7v3aj3.jpg",
    place_id=place10.id,
)

PlaceImage.create(
    url="https://avatars.mds.yandex.net/i?id=fb3b981ace05dc06756c43e0571c7e73_l-4818428-images-thumbs&n=13",
    place_id=place10.id,
)















PlaceImage.create(
    url="https://cdnn21.img.ria.ru/images/152911/18/1529111813_114:0:1874:990_1920x0_80_0_0_26344515c47cddc9d62c08b89cf4d7b2.jpg",
    place_id=place6.id,
)

PlaceImage.create(
    url="https://upload.wikimedia.org/wikipedia/commons/5/5e/Trollstigen_HochPanno.jpg",
    place_id=place6.id,
)

PlaceImage.create(
    url="https://sun9-45.userapi.com/c858132/v858132736/9ca84/vdaKPKzIJ0k.jpg",
    place_id=place5.id,
)

PlaceImage.create(
    url="https://sun9-15.userapi.com/c858132/v858132736/9ca2a/FYnw16_C_ZM.jpg",
    place_id=place5.id,
)


PlaceImage.create(
    url="https://upload.wikimedia.org/wikipedia/commons/7/7f/207_Geirangerfjord.jpg",
    place_id=place4.id,
)

PlaceImage.create(
    url="https://fotomost.com/storage/photo_1494513672_1235.jpg",
    place_id=place4.id,
)

PlaceImage.create(
    url="https://ezdiliznaem.ru/wp-content/uploads/2013/05/1e.jpg",
    place_id=place4.id,
)

PlaceImage.create(
    url="https://priroda.club/uploads/posts/2023-06/1687302454_priroda-club-p-ozero-melaren-pinterest-1.jpg",
    place_id=place1.id,
)

PlaceImage.create(
    url="https://sportishka.com/uploads/posts/2022-11/1667558316_5-sportishka-com-p-melaren-ozero-instagram-5.jpg",
    place_id=place1.id,
)

PlaceImage.create(
    url="https://img.tourister.ru/files/2/9/7/3/8/9/4/6/clones/870_600_fixedwidth.jpg",
    place_id=place2.id,
)

PlaceImage.create(
    url="https://upload.wikimedia.org/wikipedia/commons/f/f5/P1000290Jostedalsbreen.JPG",
    place_id=place3.id,
)

PlaceImage.create(
    url="https://journeying.ru/images/stories/Nigardsbreen-Norway.jpg",
    place_id=place3.id,
)



# начало --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



region1 = Region.create(
    name="Волгоградская область",
    description="Регион на юге России, известный героической обороной Сталинграда в годы Великой Отечественной войны.",
    image="https://avatars.mds.yandex.net/i?id=beb598fca2e58a15a135cdb07380c4fbe36487b2-4120632-images-thumbs&n=13"
)

region2 = Region.create(
    name="Московская область",
    description="Центральный регион России, окружающий столицу — Москву.",
    image="https://yandex-images.clstorage.net/RmqM53130/67c0e0jVIz/hOD47YPuVxNHoZFfJN8PLRAqys5uMzl3tV5p3zMgimaaWugkcWcXw8AzkxpASI_7GY2xlEYBqj3Zq55WGpJMYsbj76HAr0xGFOWNH2jYBikPYdeGbnQlJb5JctNsJYsPoS6dABkadr--TrgHFUCPrwLGptArZ-sW7_aNJlnzLj-09v7Eh_YcEWCk5VYy4C04JF7u7Wl7KjiOag7TIXHrHZIjqAc1OXGvk1elODxisbAOvqXHDnGDDOnSmA5IywsWnvj65av8FhNihuxJBPs-Ky18yM9SVwEClm8O0z57-zaVJ6khLAxxg7pBuikTRoyLCKGD0AN3gDj787MzV_IIAYDz2OK99xEEcbHLRC3EAzosVOX5T3AJKrVdNfwZcPAjmRuSBi0gTZCPSZgaG2GzgB24pu8TUJ4Czv2oF0LLPDm3-cPEuNsRMnSd2m0n-SopGF3pznBQNRypaCDoI1_aM5k3vwswAnakmHCeHBJjvJoZjKzsOl-4Hen2sxZK6h8Ei_fPxonRNRJAqsl-JtU_AT198P9KXhI8pW8n0yh60hOXO48aNS1Xn4NAkT0DeqabC4-j7ABuvw389poxevs2NbbKwei8_h05TJb3QA_COCseVfPFbl8IPZtJEeoIfesktySKBSs_d6GMfpscA3SChhiRsOEOQLgsztiWEFvOOjuH8e_GsN8KFFKk_kEhxDsvLlbiz3VmPAueWwD1K1rTM7MEsicWIFaSsFK0CSNajLsysZLJAXm5EPXPrgdOygwGmMLIw5PREjdrgs5KLNsHEgRLzOlNbyAdt1QZ8RZZ6DixAo8SLTRgsYNtpxY2X5iSFqe90A1Sjw3u_4QcdcoQJJjNx8uG1DIJWYDpZSvZPisKRfbmWFADHbdbIdU9VssphDirIQARSL6YRIw1P0eSrS6Sp8IjUrEozOy0NGfnFSiTwMfLmdMPOEuD61UK5yEFHEXWyEBfACCbUyLwNHs"
)

region3 = Region.create(
    name="Ленинградская область",
    description="Регион на северо-западе России, окружающий Санкт-Петербург.",
    image="https://avatars.mds.yandex.net/i?id=277463dab3418b10f242716d2f2621d3ba1500a6-5269099-images-thumbs&n=13"
)

region4 = Region.create(
    name="Новосибирская область",
    description="Крупный регион в Западной Сибири, центр науки и промышленности.",
    image="https://avatars.mds.yandex.net/i?id=26bbbf3069d77bcd944c88071e75ce53235d7b14-4432861-images-thumbs&n=13"
)

region5 = Region.create(
    name="Краснодарский край",
    description="Южный регион России, известный курортами на Черном море и развитым сельским хозяйством.",
    image="https://avatars.mds.yandex.net/i?id=d114a332fb0c842856e2f35471413ca2a8040da1-12625178-images-thumbs&n=13"
)

region6 = Region.create(
    name="Свердловская область",
    description="Регион на Урале, центр металлургии и машиностроения.",
    image="https://avatars.mds.yandex.net/i?id=cb3e291ce70a5c7edf8d6f1a205053b42b075d06-12752514-images-thumbs&n=13"
)

region7 = Region.create(
    name="Республика Татарстан",
    description="Республика в Поволжье с богатым культурным наследием и развитой промышленностью.",
    image="https://yandex-images.clstorage.net/RmqM53130/67c0e0jVIz/hOD47YPuVxNHoZFfJN8PLRAqys5uMzl3tV5p22Im3THIDe1zIGBAkptjwUgXTIivQo3hlhJe_mjbqsxUS5BLYcG176HErk1OFeuHCyzcCi8Nd4nfcmk9Kq8cOoBgJ-cPvy6eHQkHbbGwSY8fGkqOslSaoforGIYJ0Oq_E37xEBSF88T6mvgWPVWIz1EU9xsEMk7i2H1mIBqMYDrNNEf1PLIbmTEqAH2cqVSwNjh0kb4smbbfPXCcD_T_lwJG1Dk-i_fl1pDyFD93gdBnD-QIDRBowONRTRoCiWA60j5X3ju2Gr8oHwBRtb9LoRkcSaq4M7-h0jtzqB3V1Kodf9cuIIDV4sCb9QMsQKbdTjDZGQw4Rfb-dkUyIbtbFfU1XMs3iiGYKTM8QoC3aZIRO3ahrSqansIcbZIo28-OCEbjFheKzsTFt_U1KWy39EQN8Ao4MUnBwVZ5BD2OTgHPGnbbN6YMlTQRB3aXjm-UGDl5u6kekJ3rE0uND9DUjwBnwCsrhMLG9L3RFR1bpOdFIeUiHRFQ8PtYXiQxiUk6xD9--zmqPIQxPiZNjL5gtQkgY7q7HZ-d0SJMnRrQ_agwdukaFrnM6MGS-T4RZ5rZbDbiCD45U8rfWUQlD69_A-Q4R8wZtTmbLywGc4OAapQJLkenqAOMkN8MS7wo_vGJEUPlFCeC4sbNs-4TD1WT2EIw4QwOOkLAxGBwEwq9bhzHH3_bHZUBuRIzJ0C_rEWBKQBJmoIjrrjQNUqAE-nJngRH0yk4scXD7r32MDZzo9NPL90xJCds5vxpbAUjsncY-hxE0B-TPIwpJxFjjJNWnjwFXbOmNYGh3B58nQjZ44U_R88LOL7Ky_u41g4EcYT8SC3kCCopVunpVk8FI71PPNETZ8EqqRi_BAI5bJe6fb01HVeMngCbs_IeQrgqytOtLWrKBzOzysvkv-s_FnKGzGkT-yY8KXbH8VlMOA-1TBnYPkE"
)

region8 = Region.create(
    name="Республика Башкортостан",
    description="Республика на юге Урала, известная своей природой и нефтяной промышленностью.",
    image="https://avatars.mds.yandex.net/i?id=077506f1e38c9933bc31b158ee301280e56f0868-10375362-images-thumbs&n=13"
)

region9 = Region.create(
    name="Приморский край",
    description="Дальний Восток России, выход к Японскому морю, важный транспортный и торговый узел.",
    image="https://avatars.mds.yandex.net/i?id=aaebfe115eb67ed94d77d06266ce8ba53c8a3215-5554935-images-thumbs&n=13"
)

region10 = Region.create(
    name="Калининградская область",
    description="Эксклав России на берегу Балтийского моря, между Польшей и Литвой.",
    image="https://avatars.mds.yandex.net/i?id=e67ea56caeb5943f284713a5f33f5e9ee8cb45b2-4579694-images-thumbs&n=13"
)



regionplace1 = RegionPlace.create(
    name="Мамаев курган",
    description="Мамаев курган — мемориальный комплекс в Волгограде, посвящённый героям Сталинградской битвы. Главной достопримечательностью является статуя 'Родина-мать зовёт!', одна из самых высоких в мире. Комплекс включает в себя несколько мемориалов, музей и аллею славы.",
    latitude=48.7433,
    longitude=44.5378,
    region_id=region1.id
)
RegionPlaceImage.create(
    url="https://avatars.mds.yandex.net/i?id=f79fd98003fa9b52ac168229b0d7f6221e4bb597-2952140-images-thumbs&n=13",
    regionplace_id=regionplace1.id,
)

regionplace2 = RegionPlace.create(
    name="Адмиралтейская набережная",
    description="Адмиралтейская набережная в Воронеже — популярное место отдыха на берегу водохранилища. Здесь проходят фестивали, гуляют семьи и молодёжь, а с набережной открывается красивый вид на город. Это одна из визитных карточек Воронежа.",
    latitude=51.6615,
    longitude=39.2003,
    region_id=region2.id
)
RegionPlaceImage.create(
    url="https://avatars.mds.yandex.net/i?id=f49368f11886d540a0912f7d87de065717ce9615-4055859-images-thumbs&n=13",
    regionplace_id=regionplace2.id,
)
regionplace3 = RegionPlace.create(
    name="Курская Коренная пустынь",
    description="Курская Коренная пустынь — древний православный монастырь, расположенный в живописной лесистой местности. Основан в XIII веке, он стал духовным центром региона и ежегодно привлекает паломников и туристов со всей России.",
    latitude=51.7150,
    longitude=36.1676,
    region_id=region3.id
)
RegionPlaceImage.create(
    url="https://yandex-images.clstorage.net/RmqM53130/67c0e0jVIz/hOD47YPuVxNHoZFfJN8PLRAqys5uMzl3tV5p22QgjDLIXOx0dWwQw8k_wE1NF42sT9ntlk0P-Dnb-skGHsFFZMbluKHEpU9LFuCICyzcCi8Nd4nfcmk9Kq8cNdAhL9Ztz1yDHQcUZqm2Vb85PWCSqxSMsd1aSr4E4ruxN0LTPiSj0uHKhu8xCEi30GUz6xs_OULU50BWFju7QCTvAU7WIJs8kS4KIWGFlVKvFCR9rYI2sq7RIkmpIfTTqzFmxhY1m_fI4IjrECRCvdJnEeIECSJRx-5icDQAl2se9wRO1j-RLLopDiBHnKBSgz0yYrytEo-V1z1vvizy0J8jR-0rKqL03_6DyRcySbrFdCbFCSAdbNbvSl0CHbBjNtQ2dfkYmievJTIbYJ2MbpAIOkCPpTWwnsIkSoE81c6lFkn2Dz-bwOfJidIxN2W683EK1CAqIEXF20NRNSKQXwDIA2DtIrUNvyUeNm2ArlWkHwNGiaw3v4TGEECCFdroujFC7Q43uuPa9YfeMwZvntNFPcczKwxQ7f5jSAQYnnggxARn1imQBZ8rEgZ8hYF0nwQzSai9LqWF1BNPgi_r76okQsQpB6vK68i60B0zQLb4SQH5DQIbV8fdS0s-PJ9iIfoiUe8JlzyoCw0DY5uTVKELDUOJvSCBmMcNXI8hxeiLFmzICCaexuX5gf4zP2Gh1Vcz8AwsHVTD7UhaNCemVhf_MEDwKrAEvw8tO0GmjHWSNyFsnJ0Oj6XtLX6nLvzpty178B8zmvDY5rLZNhxvufZuFcAHIQJo_sdVdBIfr0oB1j9Z9BezP7QNKwZ0nZhDsQQef4OIC5uMyTtRviLX36o2S9oECJrs-ua91j4JapnIXBfnKCYAUcfJW04dCpBpAdYwYdA8vBylOBEiR7C9a74fN1SggRORs_EOS6wM1-GPFFjqLBq36fbtsNY-Fm2k-U4U5RgHPk7p31tuMxKfajz6OGI",
    regionplace_id=regionplace3.id,
)
regionplace4 = RegionPlace.create(
    name="Белгородская диорама",
    description="Диорама 'Курская битва. Белгородское направление' — крупнейшая в России диорама, посвящённая одному из крупнейших танковых сражений Второй мировой войны. Экспозиция включает панораму, военную технику и интерактивные выставки.",
    latitude=50.5954,
    longitude=36.5870,
    region_id=region4.id
)
RegionPlaceImage.create(
    url="https://avatars.mds.yandex.net/i?id=947e2207ef3df76076c3b611856bf04013ec0535-5701876-images-thumbs&n=13",
    regionplace_id=regionplace4.id,
)
regionplace5 = RegionPlace.create(
    name="Брянский лес",
    description="Брянский лес — биосферный заповедник с уникальной флорой и фауной. Здесь обитают редкие животные, в том числе зубры, и произрастают древние леса. Место идеально подходит для экотуризма и научных исследований.",
    latitude=52.5061,
    longitude=33.7312,
    region_id=region5.id
)
RegionPlaceImage.create(
    url="https://avatars.mds.yandex.net/i?id=ff7021949c3cd1340dae646e47b261f8295cbeb9-5086991-images-thumbs&n=13",
    regionplace_id=regionplace5.id,
)
regionplace6 = RegionPlace.create(
    name="Успенский собор",
    description="Успенский собор во Владимире — один из важнейших памятников древнерусской архитектуры, построен в XII веке. Здесь сохранились фрески Андрея Рублёва. Собор входит в список Всемирного наследия ЮНЕСКО.",
    latitude=56.1282,
    longitude=40.4070,
    region_id=region6.id
)
RegionPlaceImage.create(
    url="https://avatars.mds.yandex.net/i?id=5e265b8108541bb57fa52a3a72aae74950fe7c85-4841402-images-thumbs&n=13",
    regionplace_id=regionplace6.id,
)
regionplace7 = RegionPlace.create(
    name="Калужский планетарий",
    description="Калужский планетарий — старейший планетарий России, расположенный в городе, считающемся колыбелью отечественной космонавтики. Здесь можно познакомиться с историей звёзд и космических исследований.",
    latitude=54.5088,
    longitude=36.2527,
    region_id=region7.id
)
RegionPlaceImage.create(
    url="https://avatars.mds.yandex.net/i?id=637459623bcb68b6fea1c7684804491a9a79fb8c-5211479-images-thumbs&n=13",
    regionplace_id=regionplace7.id,
)
regionplace8 = RegionPlace.create(
    name="Липецкие минеральные источники",
    description="Минеральные источники в Липецке — курортная зона с лечебными водами, известными ещё с XVIII века. Здесь расположен санаторий, парк, питьевая галерея и фонтан, образующие уникальный природно-оздоровительный комплекс.",
    latitude=52.6104,
    longitude=39.5946,
    region_id=region8.id
)
RegionPlaceImage.create(
    url="https://avatars.mds.yandex.net/i?id=f9d40806a1daece75ea16e218b2d7879ef8e45a2-8494143-images-thumbs&n=13",
    regionplace_id=regionplace8.id,
)
regionplace9 = RegionPlace.create(
    name="Орловский краеведческий музей",
    description="Орловский краеведческий музей — один из старейших музеев региона, основанный в XIX веке. Экспозиция охватывает природу, археологию, этнографию и историю Орловской земли от древности до современности.",
    latitude=52.9688,
    longitude=36.0696,
    region_id=region9.id
)
RegionPlaceImage.create(
    url="https://avatars.mds.yandex.net/i?id=a087448c8e95ef142bc3fedd82b6f2c8ede01f5ed7d04cfb-12714748-images-thumbs&n=13",
    regionplace_id=regionplace9.id,
)
regionplace10 = RegionPlace.create(
    name="Тульский кремль",
    description="Тульский кремль — историческая крепость XVI века, расположенная в центре Тулы. Внутри находятся музеи, храмы и сувенирные лавки. Это один из самых посещаемых туристических объектов в Центральной России.",
    latitude=54.1951,
    longitude=37.6183,
    region_id=region10.id
)
RegionPlaceImage.create(
    url="https://avatars.mds.yandex.net/i?id=3e56ebb9c1ab84259a355056f24a13fbdc903598-4354006-images-thumbs&n=13",
    regionplace_id=regionplace10.id,
)

# конец --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
