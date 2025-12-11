from django.db import models

class Songs(models.Model):
    id = models.TextField(blank=True, null=True, primary_key=True)
    artist = models.TextField(blank=True, null=True)
    song = models.TextField(blank=True, null=True)
    album_name = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    # GENRES COLUMNS
    number_8_bit = models.IntegerField(db_column='8 bit', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    a_cappella = models.IntegerField(db_column='a cappella', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    abstract = models.IntegerField(blank=True, null=True)
    abstract_hip_hop = models.IntegerField(db_column='abstract hip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    accordion = models.IntegerField(blank=True, null=True)
    acid_house = models.IntegerField(db_column='acid house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    acid_jazz = models.IntegerField(db_column='acid jazz', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    acid_rock = models.IntegerField(db_column='acid rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    acoustic_blues = models.IntegerField(db_column='acoustic blues', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    acoustic_chill = models.IntegerField(db_column='acoustic chill', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    acoustic_pop = models.IntegerField(db_column='acoustic pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    acoustic_punk = models.IntegerField(db_column='acoustic punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    acoustic_rock = models.IntegerField(db_column='acoustic rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    afrikaans = models.IntegerField(blank=True, null=True)
    afro_soul = models.IntegerField(db_column='afro soul', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    afrobeat = models.IntegerField(blank=True, null=True)
    aggrotech = models.IntegerField(blank=True, null=True)
    album_rock = models.IntegerField(db_column='album rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    alternative_country = models.IntegerField(db_column='alternative country', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    alternative_dance = models.IntegerField(db_column='alternative dance', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    alternative_hip_hop = models.IntegerField(db_column='alternative hip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    alternative_metal = models.IntegerField(db_column='alternative metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    alternative_pop = models.IntegerField(db_column='alternative pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    alternative_pop_rock = models.IntegerField(db_column='alternative pop rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    alternative_rock = models.IntegerField(db_column='alternative rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ambient = models.IntegerField(blank=True, null=True)
    ambient_black_metal = models.IntegerField(db_column='ambient black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ambient_house = models.IntegerField(db_column='ambient house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ambient_pop = models.IntegerField(db_column='ambient pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ambient_techno = models.IntegerField(db_column='ambient techno', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ambient_trance = models.IntegerField(db_column='ambient trance', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    anarcho_punk = models.IntegerField(db_column='anarcho punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    anime = models.IntegerField(blank=True, null=True)
    anthem = models.IntegerField(blank=True, null=True)
    anti_folk = models.IntegerField(db_column='anti folk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    appalachian_folk = models.IntegerField(db_column='appalachian folk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    art_pop = models.IntegerField(db_column='art pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    art_punk = models.IntegerField(db_column='art punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    art_rock = models.IntegerField(db_column='art rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    asmr = models.IntegerField(blank=True, null=True)
    atmosphere = models.IntegerField(blank=True, null=True)
    atmospheric_black_metal = models.IntegerField(db_column='atmospheric black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    atmospheric_doom = models.IntegerField(db_column='atmospheric doom', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    atmospheric_sludge = models.IntegerField(db_column='atmospheric sludge', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    australian_hardcore = models.IntegerField(db_column='australian hardcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    australian_house = models.IntegerField(db_column='australian house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    australian_metalcore = models.IntegerField(db_column='australian metalcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    australian_rock = models.IntegerField(db_column='australian rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    austrian_black_metal = models.IntegerField(db_column='austrian black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    avant_garde = models.IntegerField(db_column='avant garde', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    avant_garde_black_metal = models.IntegerField(db_column='avant garde black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    avant_garde_metal = models.IntegerField(db_column='avant garde metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    avant_rock = models.IntegerField(db_column='avant rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    axe = models.IntegerField(blank=True, null=True)
    bachata = models.IntegerField(blank=True, null=True)
    background_music = models.IntegerField(db_column='background music', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    bagpipe = models.IntegerField(blank=True, null=True)
    baiao = models.IntegerField(blank=True, null=True)
    balearic = models.IntegerField(blank=True, null=True)
    ballroom = models.IntegerField(blank=True, null=True)
    banjo = models.IntegerField(blank=True, null=True)
    bard = models.IntegerField(blank=True, null=True)
    baroque = models.IntegerField(blank=True, null=True)
    baroque_pop = models.IntegerField(db_column='baroque pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    bassline = models.IntegerField(blank=True, null=True)
    batida = models.IntegerField(blank=True, null=True)
    beach_music = models.IntegerField(db_column='beach music', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beat_poetry = models.IntegerField(db_column='beat poetry', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    beatdown = models.IntegerField(blank=True, null=True)
    beatlesque = models.IntegerField(blank=True, null=True)
    beats = models.IntegerField(blank=True, null=True)
    bebop = models.IntegerField(blank=True, null=True)
    bedroom_pop = models.IntegerField(db_column='bedroom pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    bells = models.IntegerField(blank=True, null=True)
    bible = models.IntegerField(blank=True, null=True)
    big_band = models.IntegerField(db_column='big band', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    big_beat = models.IntegerField(db_column='big beat', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    birthday = models.IntegerField(blank=True, null=True)
    bitpop = models.IntegerField(blank=True, null=True)
    black_metal = models.IntegerField(db_column='black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    black_n_roll = models.IntegerField(db_column='black n roll', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    black_punk = models.IntegerField(db_column='black punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    black_thrash = models.IntegerField(db_column='black thrash', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    blackened_crust = models.IntegerField(db_column='blackened crust', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    blackened_deathcore = models.IntegerField(db_column='blackened deathcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    blackgaze = models.IntegerField(blank=True, null=True)
    bluegrass = models.IntegerField(blank=True, null=True)
    blues = models.IntegerField(blank=True, null=True)
    blues_rock = models.IntegerField(db_column='blues rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    bolero = models.IntegerField(blank=True, null=True)
    bomba = models.IntegerField(blank=True, null=True)
    boogie = models.IntegerField(blank=True, null=True)
    boom_bap = models.IntegerField(db_column='boom bap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    bossa_nova = models.IntegerField(db_column='bossa nova', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    boston_hardcore = models.IntegerField(db_column='boston hardcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    bounce = models.IntegerField(blank=True, null=True)
    boy_band = models.IntegerField(db_column='boy band', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    braindance = models.IntegerField(blank=True, null=True)
    brazilian_death_metal = models.IntegerField(db_column='brazilian death metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    brazilian_metal = models.IntegerField(db_column='brazilian metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    brazilian_rock = models.IntegerField(db_column='brazilian rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    breakbeat = models.IntegerField(blank=True, null=True)
    breaks = models.IntegerField(blank=True, null=True)
    brill_building_pop = models.IntegerField(db_column='brill building pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    british_blues = models.IntegerField(db_column='british blues', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    british_death_metal = models.IntegerField(db_column='british death metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    british_invasion = models.IntegerField(db_column='british invasion', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    british_soul = models.IntegerField(db_column='british soul', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    britpop = models.IntegerField(blank=True, null=True)
    broadway = models.IntegerField(blank=True, null=True)
    broken_beat = models.IntegerField(db_column='broken beat', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    brostep = models.IntegerField(blank=True, null=True)
    brutal_death_metal = models.IntegerField(db_column='brutal death metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    brutal_deathcore = models.IntegerField(db_column='brutal deathcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    bubblegum_dance = models.IntegerField(db_column='bubblegum dance', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    bubblegum_pop = models.IntegerField(db_column='bubblegum pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    c64 = models.IntegerField(blank=True, null=True)
    c86 = models.IntegerField(blank=True, null=True)
    cabaret = models.IntegerField(blank=True, null=True)
    cajun = models.IntegerField(blank=True, null=True)
    canadian_death_metal = models.IntegerField(db_column='canadian death metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    canadian_indie = models.IntegerField(db_column='canadian indie', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    canadian_metal = models.IntegerField(db_column='canadian metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    canadian_pop = models.IntegerField(db_column='canadian pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    canadian_punk = models.IntegerField(db_column='canadian punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    canadian_rock = models.IntegerField(db_column='canadian rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cantaditas = models.IntegerField(blank=True, null=True)
    cantautor = models.IntegerField(blank=True, null=True)
    canterbury_scene = models.IntegerField(db_column='canterbury scene', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    capoeira = models.IntegerField(blank=True, null=True)
    carnaval = models.IntegerField(blank=True, null=True)
    cartoon = models.IntegerField(blank=True, null=True)
    ccm = models.IntegerField(blank=True, null=True)
    cello = models.IntegerField(blank=True, null=True)
    celtic = models.IntegerField(blank=True, null=True)
    celtic_metal = models.IntegerField(db_column='celtic metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    celtic_punk = models.IntegerField(db_column='celtic punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    celtic_rock = models.IntegerField(db_column='celtic rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    chamber_pop = models.IntegerField(db_column='chamber pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    chanson = models.IntegerField(blank=True, null=True)
    chaotic_hardcore = models.IntegerField(db_column='chaotic hardcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    chicago_blues = models.IntegerField(db_column='chicago blues', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    chilean_indie = models.IntegerField(db_column='chilean indie', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    chilean_rock = models.IntegerField(db_column='chilean rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    chilena = models.IntegerField(blank=True, null=True)
    chill_beats = models.IntegerField(db_column='chill beats', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    chill_groove = models.IntegerField(db_column='chill groove', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    chill_out = models.IntegerField(db_column='chill out', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    chillstep = models.IntegerField(blank=True, null=True)
    chillwave = models.IntegerField(blank=True, null=True)
    chiptune = models.IntegerField(blank=True, null=True)
    choral = models.IntegerField(blank=True, null=True)
    choro = models.IntegerField(blank=True, null=True)
    christian_hard_rock = models.IntegerField(db_column='christian hard rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    christian_hardcore = models.IntegerField(db_column='christian hardcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    christian_metal = models.IntegerField(db_column='christian metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    christian_metalcore = models.IntegerField(db_column='christian metalcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    christian_music = models.IntegerField(db_column='christian music', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    christian_pop = models.IntegerField(db_column='christian pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    christian_punk = models.IntegerField(db_column='christian punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    christian_rock = models.IntegerField(db_column='christian rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    circus = models.IntegerField(blank=True, null=True)
    city_pop = models.IntegerField(db_column='city pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    classic_house = models.IntegerField(db_column='classic house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    classic_rock = models.IntegerField(db_column='classic rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    classic_soul = models.IntegerField(db_column='classic soul', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    classical = models.IntegerField(blank=True, null=True)
    classical_guitar = models.IntegerField(db_column='classical guitar', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    coco = models.IntegerField(blank=True, null=True)
    coldwave = models.IntegerField(blank=True, null=True)
    comedy = models.IntegerField(blank=True, null=True)
    comedy_rock = models.IntegerField(db_column='comedy rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    complextro = models.IntegerField(blank=True, null=True)
    conscious_hip_hop = models.IntegerField(db_column='conscious hip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    contemporary_classical = models.IntegerField(db_column='contemporary classical', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    contemporary_country = models.IntegerField(db_column='contemporary country', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    contemporary_folk = models.IntegerField(db_column='contemporary folk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    contemporary_gospel = models.IntegerField(db_column='contemporary gospel', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    contemporary_jazz = models.IntegerField(db_column='contemporary jazz', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cool_jazz = models.IntegerField(db_column='cool jazz', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    country = models.IntegerField(blank=True, null=True)
    country_blues = models.IntegerField(db_column='country blues', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    country_gospel = models.IntegerField(db_column='country gospel', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    country_pop = models.IntegerField(db_column='country pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    country_rap = models.IntegerField(db_column='country rap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    country_rock = models.IntegerField(db_column='country rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cowpunk = models.IntegerField(blank=True, null=True)
    crossover_prog = models.IntegerField(db_column='crossover prog', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    crossover_thrash = models.IntegerField(db_column='crossover thrash', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    crunk = models.IntegerField(blank=True, null=True)
    crust_punk = models.IntegerField(db_column='crust punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cuarteto = models.IntegerField(blank=True, null=True)
    cumbia = models.IntegerField(blank=True, null=True)
    cybergrind = models.IntegerField(blank=True, null=True)
    cyberpunk = models.IntegerField(blank=True, null=True)
    d_beat = models.IntegerField(db_column='d beat', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dance_pop = models.IntegerField(db_column='dance pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dance_punk = models.IntegerField(db_column='dance punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dance_rock = models.IntegerField(db_column='dance rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dancehall = models.IntegerField(blank=True, null=True)
    dark_ambient = models.IntegerField(db_column='dark ambient', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dark_black_metal = models.IntegerField(db_column='dark black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dark_cabaret = models.IntegerField(db_column='dark cabaret', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dark_disco = models.IntegerField(db_column='dark disco', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dark_electro = models.IntegerField(db_column='dark electro', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dark_electro_industrial = models.IntegerField(db_column='dark electro industrial', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dark_folk = models.IntegerField(db_column='dark folk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dark_hardcore = models.IntegerField(db_column='dark hardcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dark_rock = models.IntegerField(db_column='dark rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dark_trap = models.IntegerField(db_column='dark trap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dark_wave = models.IntegerField(db_column='dark wave', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    darkstep = models.IntegerField(blank=True, null=True)
    darksynth = models.IntegerField(blank=True, null=True)
    dc_hardcore = models.IntegerField(db_column='dc hardcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    death_doom = models.IntegerField(db_column='death doom', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    death_metal = models.IntegerField(db_column='death metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    death_n_roll = models.IntegerField(db_column='death n roll', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    deathcore = models.IntegerField(blank=True, null=True)
    deathgrind = models.IntegerField(blank=True, null=True)
    deathrock = models.IntegerField(blank=True, null=True)
    deathstep = models.IntegerField(blank=True, null=True)
    deconstructed_club = models.IntegerField(db_column='deconstructed club', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    deep_ambient = models.IntegerField(db_column='deep ambient', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    deep_house = models.IntegerField(db_column='deep house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    deep_techno = models.IntegerField(db_column='deep techno', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    delta_blues = models.IntegerField(db_column='delta blues', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demoscene = models.IntegerField(blank=True, null=True)
    depressive_black_metal = models.IntegerField(db_column='depressive black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    detroit_hip_hop = models.IntegerField(db_column='detroit hip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    deutschrock = models.IntegerField(blank=True, null=True)
    digital_hardcore = models.IntegerField(db_column='digital hardcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dirty_south_rap = models.IntegerField(db_column='dirty south rap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    disco = models.IntegerField(blank=True, null=True)
    disco_house = models.IntegerField(db_column='disco house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    discofox = models.IntegerField(blank=True, null=True)
    disney = models.IntegerField(blank=True, null=True)
    diva_house = models.IntegerField(db_column='diva house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    djent = models.IntegerField(blank=True, null=True)
    doo_wop = models.IntegerField(db_column='doo wop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    doom_metal = models.IntegerField(db_column='doom metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    doomgaze = models.IntegerField(blank=True, null=True)
    doujin = models.IntegerField(blank=True, null=True)
    downtempo = models.IntegerField(blank=True, null=True)
    drama = models.IntegerField(blank=True, null=True)
    dream_pop = models.IntegerField(db_column='dream pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dream_trance = models.IntegerField(db_column='dream trance', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dreamgaze = models.IntegerField(blank=True, null=True)
    drill = models.IntegerField(blank=True, null=True)
    drone = models.IntegerField(blank=True, null=True)
    drone_metal = models.IntegerField(db_column='drone metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    drone_rock = models.IntegerField(db_column='drone rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    drum_and_bass = models.IntegerField(db_column='drum and bass', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dub = models.IntegerField(blank=True, null=True)
    dub_reggae = models.IntegerField(db_column='dub reggae', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dubstep = models.IntegerField(blank=True, null=True)
    dutch_metal = models.IntegerField(db_column='dutch metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    early_music = models.IntegerField(db_column='early music', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    early_reggae = models.IntegerField(db_column='early reggae', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    east_coast_hip_hop = models.IntegerField(db_column='east coast hip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    easy_listening = models.IntegerField(db_column='easy listening', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    easycore = models.IntegerField(blank=True, null=True)
    ebm = models.IntegerField(blank=True, null=True)
    edm = models.IntegerField(blank=True, null=True)
    electric_bass = models.IntegerField(db_column='electric bass', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    electric_blues = models.IntegerField(db_column='electric blues', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    electro = models.IntegerField(blank=True, null=True)
    electro_house = models.IntegerField(db_column='electro house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    electro_industrial = models.IntegerField(db_column='electro industrial', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    electro_jazz = models.IntegerField(db_column='electro jazz', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    electro_latino = models.IntegerField(db_column='electro latino', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    electro_swing = models.IntegerField(db_column='electro swing', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    electroclash = models.IntegerField(blank=True, null=True)
    electronic_rock = models.IntegerField(db_column='electronic rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    electronica = models.IntegerField(blank=True, null=True)
    electronicore = models.IntegerField(blank=True, null=True)
    electropop = models.IntegerField(blank=True, null=True)
    elektropunk = models.IntegerField(blank=True, null=True)
    elephant_6 = models.IntegerField(db_column='elephant 6', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    emo = models.IntegerField(blank=True, null=True)
    emo_punk = models.IntegerField(db_column='emo punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    emo_rap = models.IntegerField(db_column='emo rap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    emocore = models.IntegerField(blank=True, null=True)
    environmental = models.IntegerField(blank=True, null=True)
    epic_black_metal = models.IntegerField(db_column='epic black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    epic_doom = models.IntegerField(db_column='epic doom', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    erotica = models.IntegerField(blank=True, null=True)
    estonian_pop = models.IntegerField(db_column='estonian pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ethereal_wave = models.IntegerField(db_column='ethereal wave', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    eurobeat = models.IntegerField(blank=True, null=True)
    eurodance = models.IntegerField(blank=True, null=True)
    europop = models.IntegerField(blank=True, null=True)
    eurovision = models.IntegerField(blank=True, null=True)
    exotica = models.IntegerField(blank=True, null=True)
    experimental = models.IntegerField(blank=True, null=True)
    experimental_ambient = models.IntegerField(db_column='experimental ambient', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    experimental_black_metal = models.IntegerField(db_column='experimental black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    experimental_hip_hop = models.IntegerField(db_column='experimental hip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    experimental_pop = models.IntegerField(db_column='experimental pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    experimental_rock = models.IntegerField(db_column='experimental rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    fado = models.IntegerField(blank=True, null=True)
    fake = models.IntegerField(blank=True, null=True)
    fast_melodic_punk = models.IntegerField(db_column='fast melodic punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    final_fantasy = models.IntegerField(db_column='final fantasy', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    finnish_black_metal = models.IntegerField(db_column='finnish black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    finnish_metal = models.IntegerField(db_column='finnish metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    finnish_pop = models.IntegerField(db_column='finnish pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    finnish_power_metal = models.IntegerField(db_column='finnish power metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    flamenco = models.IntegerField(blank=True, null=True)
    flamenco_fusion = models.IntegerField(db_column='flamenco fusion', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    florida_death_metal = models.IntegerField(db_column='florida death metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    focus = models.IntegerField(blank=True, null=True)
    folk = models.IntegerField(blank=True, null=True)
    folk_black_metal = models.IntegerField(db_column='folk black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    folk_metal = models.IntegerField(db_column='folk metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    folk_pop = models.IntegerField(db_column='folk pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    folk_punk = models.IntegerField(db_column='folk punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    folk_rock = models.IntegerField(db_column='folk rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    folktronica = models.IntegerField(blank=True, null=True)
    football = models.IntegerField(blank=True, null=True)
    forest_black_metal = models.IntegerField(db_column='forest black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    forro = models.IntegerField(blank=True, null=True)
    freak_folk = models.IntegerField(db_column='freak folk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    freakbeat = models.IntegerField(blank=True, null=True)
    free_jazz = models.IntegerField(db_column='free jazz', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    freestyle = models.IntegerField(blank=True, null=True)
    french_black_metal = models.IntegerField(db_column='french black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    french_folk = models.IntegerField(db_column='french folk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    french_metal = models.IntegerField(db_column='french metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    french_pop = models.IntegerField(db_column='french pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    french_rock = models.IntegerField(db_column='french rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    full_on = models.IntegerField(db_column='full on', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    funeral_doom = models.IntegerField(db_column='funeral doom', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    funk = models.IntegerField(blank=True, null=True)
    funk_metal = models.IntegerField(db_column='funk metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    funk_pop = models.IntegerField(db_column='funk pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    funk_rock = models.IntegerField(db_column='funk rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    funky_breaks = models.IntegerField(db_column='funky breaks', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    funky_house = models.IntegerField(db_column='funky house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    future_bass = models.IntegerField(db_column='future bass', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    future_garage = models.IntegerField(db_column='future garage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    future_house = models.IntegerField(db_column='future house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    future_rock = models.IntegerField(db_column='future rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    futurepop = models.IntegerField(blank=True, null=True)
    g_funk = models.IntegerField(db_column='g funk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    garage_pop = models.IntegerField(db_column='garage pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    garage_punk = models.IntegerField(db_column='garage punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    garage_rock = models.IntegerField(db_column='garage rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    garage_rock_revival = models.IntegerField(db_column='garage rock revival', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    geek_rock = models.IntegerField(db_column='geek rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    german_death_metal = models.IntegerField(db_column='german death metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    german_hard_rock = models.IntegerField(db_column='german hard rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    german_heavy_metal = models.IntegerField(db_column='german heavy metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    german_hip_hop = models.IntegerField(db_column='german hip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    german_indie = models.IntegerField(db_column='german indie', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    german_metal = models.IntegerField(db_column='german metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    german_metalcore = models.IntegerField(db_column='german metalcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    german_pop_rock = models.IntegerField(db_column='german pop rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    german_rock = models.IntegerField(db_column='german rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    german_thrash_metal = models.IntegerField(db_column='german thrash metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ghettotech = models.IntegerField(blank=True, null=True)
    girl_group = models.IntegerField(db_column='girl group', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    glam_metal = models.IntegerField(db_column='glam metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    glam_punk = models.IntegerField(db_column='glam punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    glam_rock = models.IntegerField(db_column='glam rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    glass = models.IntegerField(blank=True, null=True)
    glitch = models.IntegerField(blank=True, null=True)
    glitch_hop = models.IntegerField(db_column='glitch hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    glitch_pop = models.IntegerField(db_column='glitch pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    goa_trance = models.IntegerField(db_column='goa trance', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    golden_age_hip_hop = models.IntegerField(db_column='golden age hip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    goregrind = models.IntegerField(blank=True, null=True)
    gospel = models.IntegerField(blank=True, null=True)
    gospel_rap = models.IntegerField(db_column='gospel rap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gospel_soul = models.IntegerField(db_column='gospel soul', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gothabilly = models.IntegerField(blank=True, null=True)
    gothenburg_metal = models.IntegerField(db_column='gothenburg metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gothic_americana = models.IntegerField(db_column='gothic americana', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gothic_black_metal = models.IntegerField(db_column='gothic black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gothic_doom = models.IntegerField(db_column='gothic doom', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gothic_metal = models.IntegerField(db_column='gothic metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gothic_rock = models.IntegerField(db_column='gothic rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    greek_metal = models.IntegerField(db_column='greek metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    greek_pop = models.IntegerField(db_column='greek pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    grime = models.IntegerField(blank=True, null=True)
    grindcore = models.IntegerField(blank=True, null=True)
    groove_metal = models.IntegerField(db_column='groove metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    grunge = models.IntegerField(blank=True, null=True)
    gypsy = models.IntegerField(blank=True, null=True)
    gypsy_jazz = models.IntegerField(db_column='gypsy jazz', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gypsy_punk = models.IntegerField(db_column='gypsy punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    halloween = models.IntegerField(blank=True, null=True)
    hamburg_hip_hop = models.IntegerField(db_column='hamburg hip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hamburger_schule = models.IntegerField(db_column='hamburger schule', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hammered_dulcimer = models.IntegerField(db_column='hammered dulcimer', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    happy_hardcore = models.IntegerField(db_column='happy hardcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hard_alternative = models.IntegerField(db_column='hard alternative', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hard_bass = models.IntegerField(db_column='hard bass', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hard_bop = models.IntegerField(db_column='hard bop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hard_house = models.IntegerField(db_column='hard house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hard_rock = models.IntegerField(db_column='hard rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hard_trance = models.IntegerField(db_column='hard trance', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hardcore = models.IntegerField(blank=True, null=True)
    hardcore_hip_hop = models.IntegerField(db_column='hardcore hip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hardcore_punk = models.IntegerField(db_column='hardcore punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hardstyle = models.IntegerField(blank=True, null=True)
    harmonica_blues = models.IntegerField(db_column='harmonica blues', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    harp = models.IntegerField(blank=True, null=True)
    harpsichord = models.IntegerField(blank=True, null=True)
    hauntology = models.IntegerField(blank=True, null=True)
    hawaiian = models.IntegerField(blank=True, null=True)
    healing = models.IntegerField(blank=True, null=True)
    heartland_rock = models.IntegerField(db_column='heartland rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    heavy_psych = models.IntegerField(db_column='heavy psych', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hi_nrg = models.IntegerField(db_column='hi nrg', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hip_hop = models.IntegerField(db_column='hip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hip_house = models.IntegerField(db_column='hip house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hip_pop = models.IntegerField(db_column='hip pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hollywood = models.IntegerField(blank=True, null=True)
    honky_tonk = models.IntegerField(db_column='honky tonk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    horror_punk = models.IntegerField(db_column='horror punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    horrorcore = models.IntegerField(blank=True, null=True)
    house = models.IntegerField(blank=True, null=True)
    hurdy_gurdy = models.IntegerField(db_column='hurdy gurdy', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hyperpop = models.IntegerField(blank=True, null=True)
    hyphy = models.IntegerField(blank=True, null=True)
    hypnosis = models.IntegerField(blank=True, null=True)
    idol = models.IntegerField(blank=True, null=True)
    indie_electronica = models.IntegerField(db_column='indie electronica', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    indie_emo = models.IntegerField(db_column='indie emo', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    indie_folk = models.IntegerField(db_column='indie folk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    indie_hip_hop = models.IntegerField(db_column='indie hip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    indie_pop = models.IntegerField(db_column='indie pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    indie_pop_rock = models.IntegerField(db_column='indie pop rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    indie_poptimism = models.IntegerField(db_column='indie poptimism', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    indie_punk = models.IntegerField(db_column='indie punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    indie_rock = models.IntegerField(db_column='indie rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    indie_surf = models.IntegerField(db_column='indie surf', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    indietronica = models.IntegerField(blank=True, null=True)
    industrial = models.IntegerField(blank=True, null=True)
    industrial_black_metal = models.IntegerField(db_column='industrial black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    industrial_hip_hop = models.IntegerField(db_column='industrial hip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    industrial_metal = models.IntegerField(db_column='industrial metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    industrial_rock = models.IntegerField(db_column='industrial rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    industrial_techno = models.IntegerField(db_column='industrial techno', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    instrumental_rock = models.IntegerField(db_column='instrumental rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    intelligent_dance_music = models.IntegerField(db_column='intelligent dance music', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    irish_folk = models.IntegerField(db_column='irish folk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    irish_pop = models.IntegerField(db_column='irish pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    irish_rock = models.IntegerField(db_column='irish rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    italian_doom_metal = models.IntegerField(db_column='italian doom metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    italian_metal = models.IntegerField(db_column='italian metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    italian_pop = models.IntegerField(db_column='italian pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    italo_house = models.IntegerField(db_column='italo house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    j_metal = models.IntegerField(db_column='j metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    j_pop = models.IntegerField(db_column='j pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    j_rock = models.IntegerField(db_column='j rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    jam_band = models.IntegerField(db_column='jam band', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    jangle_pop = models.IntegerField(db_column='jangle pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    jazz = models.IntegerField(blank=True, null=True)
    jazz_blues = models.IntegerField(db_column='jazz blues', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    jazz_funk = models.IntegerField(db_column='jazz funk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    jazz_fusion = models.IntegerField(db_column='jazz fusion', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    jazz_guitar = models.IntegerField(db_column='jazz guitar', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    jazz_house = models.IntegerField(db_column='jazz house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    jazz_piano = models.IntegerField(db_column='jazz piano', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    jazz_pop = models.IntegerField(db_column='jazz pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    jazz_rap = models.IntegerField(db_column='jazz rap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    jazz_rock = models.IntegerField(db_column='jazz rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    jazz_vibraphone = models.IntegerField(db_column='jazz vibraphone', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    jazzcore = models.IntegerField(blank=True, null=True)
    jovem_guarda = models.IntegerField(db_column='jovem guarda', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    jump_up = models.IntegerField(db_column='jump up', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    jungle = models.IntegerField(blank=True, null=True)
    k_pop = models.IntegerField(db_column='k pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    k_rock = models.IntegerField(db_column='k rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    karaoke = models.IntegerField(blank=True, null=True)
    klezmer = models.IntegerField(blank=True, null=True)
    korean_pop = models.IntegerField(db_column='korean pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    krautrock = models.IntegerField(blank=True, null=True)
    kuduro = models.IntegerField(blank=True, null=True)
    latin = models.IntegerField(blank=True, null=True)
    latin_alternative = models.IntegerField(db_column='latin alternative', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    latin_hip_hop = models.IntegerField(db_column='latin hip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    latin_jazz = models.IntegerField(db_column='latin jazz', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    latin_metal = models.IntegerField(db_column='latin metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    latin_pop = models.IntegerField(db_column='latin pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    latin_rock = models.IntegerField(db_column='latin rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    liedermacher = models.IntegerField(blank=True, null=True)
    light_music = models.IntegerField(db_column='light music', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    liquid_funk = models.IntegerField(db_column='liquid funk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    lo_fi = models.IntegerField(db_column='lo fi', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    lo_fi_indie = models.IntegerField(db_column='lo fi indie', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    lounge = models.IntegerField(blank=True, null=True)
    louvor = models.IntegerField(blank=True, null=True)
    lovers_rock = models.IntegerField(db_column='lovers rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    lullaby = models.IntegerField(blank=True, null=True)
    madchester = models.IntegerField(blank=True, null=True)
    maghreb = models.IntegerField(blank=True, null=True)
    mandolin = models.IntegerField(blank=True, null=True)
    mantra = models.IntegerField(blank=True, null=True)
    mariachi = models.IntegerField(blank=True, null=True)
    martial_industrial = models.IntegerField(db_column='martial industrial', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mashup = models.IntegerField(blank=True, null=True)
    massage = models.IntegerField(blank=True, null=True)
    math_rock = models.IntegerField(db_column='math rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mathcore = models.IntegerField(blank=True, null=True)
    medieval = models.IntegerField(blank=True, null=True)
    medieval_folk = models.IntegerField(db_column='medieval folk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    medieval_rock = models.IntegerField(db_column='medieval rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    meditation = models.IntegerField(blank=True, null=True)
    melancholia = models.IntegerField(blank=True, null=True)
    mellow_gold = models.IntegerField(db_column='mellow gold', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    melodic_black_metal = models.IntegerField(db_column='melodic black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    melodic_death_metal = models.IntegerField(db_column='melodic death metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    melodic_deathcore = models.IntegerField(db_column='melodic deathcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    melodic_hard_rock = models.IntegerField(db_column='melodic hard rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    melodic_hardcore = models.IntegerField(db_column='melodic hardcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    melodic_metal = models.IntegerField(db_column='melodic metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    melodic_metalcore = models.IntegerField(db_column='melodic metalcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    melodic_power_metal = models.IntegerField(db_column='melodic power metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    melodic_progressive_metal = models.IntegerField(db_column='melodic progressive metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    memphis_soul = models.IntegerField(db_column='memphis soul', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    merengue = models.IntegerField(blank=True, null=True)
    merseybeat = models.IntegerField(blank=True, null=True)
    metal = models.IntegerField(blank=True, null=True)
    metal_gotico = models.IntegerField(db_column='metal gotico', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    metalcore = models.IntegerField(blank=True, null=True)
    metallic_hardcore = models.IntegerField(db_column='metallic hardcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mexican_pop = models.IntegerField(db_column='mexican pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mexican_rock = models.IntegerField(db_column='mexican rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    miami_bass = models.IntegerField(db_column='miami bass', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    middle_earth = models.IntegerField(db_column='middle earth', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    midwest_emo = models.IntegerField(db_column='midwest emo', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    minimal_synth = models.IntegerField(db_column='minimal synth', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    minimal_techno = models.IntegerField(db_column='minimal techno', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    minimal_wave = models.IntegerField(db_column='minimal wave', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    minimalism = models.IntegerField(blank=True, null=True)
    minneapolis_sound = models.IntegerField(db_column='minneapolis sound', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mod_revival = models.IntegerField(db_column='mod revival', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    modern_blues = models.IntegerField(db_column='modern blues', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    modern_hard_rock = models.IntegerField(db_column='modern hard rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    modern_rock = models.IntegerField(db_column='modern rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    moog = models.IntegerField(blank=True, null=True)
    motivation = models.IntegerField(blank=True, null=True)
    motown = models.IntegerField(blank=True, null=True)
    mpb = models.IntegerField(blank=True, null=True)
    music_hall = models.IntegerField(db_column='music hall', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nashville_sound = models.IntegerField(db_column='nashville sound', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    native_american = models.IntegerField(db_column='native american', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    neo_classical = models.IntegerField(db_column='neo classical', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    neo_classical_metal = models.IntegerField(db_column='neo classical metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    neo_metal = models.IntegerField(db_column='neo metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    neo_progressive = models.IntegerField(db_column='neo progressive', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    neo_psychedelic = models.IntegerField(db_column='neo psychedelic', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    neo_soul = models.IntegerField(db_column='neo soul', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    neoclassical_darkwave = models.IntegerField(db_column='neoclassical darkwave', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    neofolk = models.IntegerField(blank=True, null=True)
    nerdcore = models.IntegerField(blank=True, null=True)
    neue_deutsche_harte = models.IntegerField(db_column='neue deutsche harte', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    neurofunk = models.IntegerField(blank=True, null=True)
    new_age = models.IntegerField(db_column='new age', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_americana = models.IntegerField(db_column='new americana', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_beat = models.IntegerField(db_column='new beat', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_jack_swing = models.IntegerField(db_column='new jack swing', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_orleans_funk = models.IntegerField(db_column='new orleans funk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_rave = models.IntegerField(db_column='new rave', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_romantic = models.IntegerField(db_column='new romantic', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_wave = models.IntegerField(db_column='new wave', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_wave_pop = models.IntegerField(db_column='new wave pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    new_weird_america = models.IntegerField(db_column='new weird america', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nintendocore = models.IntegerField(blank=True, null=True)
    no_wave = models.IntegerField(db_column='no wave', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    noise = models.IntegerField(blank=True, null=True)
    noise_pop = models.IntegerField(db_column='noise pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    noise_punk = models.IntegerField(db_column='noise punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    noise_rock = models.IntegerField(db_column='noise rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    noisecore = models.IntegerField(blank=True, null=True)
    nordic_folk = models.IntegerField(db_column='nordic folk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    northern_soul = models.IntegerField(db_column='northern soul', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    norwegian_black_metal = models.IntegerField(db_column='norwegian black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    norwegian_metal = models.IntegerField(db_column='norwegian metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    norwegian_pop = models.IntegerField(db_column='norwegian pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nouvelle_chanson_francaise = models.IntegerField(db_column='nouvelle chanson francaise', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nova_mpb = models.IntegerField(db_column='nova mpb', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    novelty = models.IntegerField(blank=True, null=True)
    nu_disco = models.IntegerField(db_column='nu disco', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nu_electro = models.IntegerField(db_column='nu electro', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nu_gaze = models.IntegerField(db_column='nu gaze', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nu_jazz = models.IntegerField(db_column='nu jazz', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nu_metal = models.IntegerField(db_column='nu metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nuevo_flamenco = models.IntegerField(db_column='nuevo flamenco', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nwobhm = models.IntegerField(blank=True, null=True)
    nwothm = models.IntegerField(blank=True, null=True)
    ocean = models.IntegerField(blank=True, null=True)
    oi = models.IntegerField(blank=True, null=True)
    old_school_hip_hop = models.IntegerField(db_column='old school hip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    old_school_thrash = models.IntegerField(db_column='old school thrash', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    old_time = models.IntegerField(db_column='old time', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    opera = models.IntegerField(blank=True, null=True)
    opera_metal = models.IntegerField(db_column='opera metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    operatic_pop = models.IntegerField(db_column='operatic pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    opm = models.IntegerField(blank=True, null=True)
    orchestra = models.IntegerField(blank=True, null=True)
    organic_ambient = models.IntegerField(db_column='organic ambient', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    oriental_metal = models.IntegerField(db_column='oriental metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    outlaw_country = models.IntegerField(db_column='outlaw country', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    outsider = models.IntegerField(blank=True, null=True)
    p_funk = models.IntegerField(db_column='p funk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pagan_black_metal = models.IntegerField(db_column='pagan black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pagode = models.IntegerField(blank=True, null=True)
    parody = models.IntegerField(blank=True, null=True)
    philly_soul = models.IntegerField(db_column='philly soul', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    piano_blues = models.IntegerField(db_column='piano blues', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    piano_rock = models.IntegerField(db_column='piano rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pinoy_rock = models.IntegerField(db_column='pinoy rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pixie = models.IntegerField(blank=True, null=True)
    plunderphonics = models.IntegerField(blank=True, null=True)
    poetry = models.IntegerField(blank=True, null=True)
    poezja_spiewana = models.IntegerField(db_column='poezja spiewana', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polish_black_metal = models.IntegerField(db_column='polish black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polish_death_metal = models.IntegerField(db_column='polish death metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polish_jazz = models.IntegerField(db_column='polish jazz', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polish_metal = models.IntegerField(db_column='polish metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polish_pop = models.IntegerField(db_column='polish pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polish_prog = models.IntegerField(db_column='polish prog', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polish_punk = models.IntegerField(db_column='polish punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polish_rock = models.IntegerField(db_column='polish rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polka = models.IntegerField(blank=True, null=True)
    pony = models.IntegerField(blank=True, null=True)
    pop = models.IntegerField(blank=True, null=True)
    pop_chileno = models.IntegerField(db_column='pop chileno', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pop_dance = models.IntegerField(db_column='pop dance', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pop_emo = models.IntegerField(db_column='pop emo', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pop_folk = models.IntegerField(db_column='pop folk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pop_house = models.IntegerField(db_column='pop house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pop_nacional = models.IntegerField(db_column='pop nacional', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pop_punk = models.IntegerField(db_column='pop punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pop_rap = models.IntegerField(db_column='pop rap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pop_rock = models.IntegerField(db_column='pop rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pop_romantico = models.IntegerField(db_column='pop romantico', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pop_soul = models.IntegerField(db_column='pop soul', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pornogrind = models.IntegerField(blank=True, null=True)
    post_black_metal = models.IntegerField(db_column='post black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    post_disco = models.IntegerField(db_column='post disco', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    post_grunge = models.IntegerField(db_column='post grunge', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    post_hardcore = models.IntegerField(db_column='post hardcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    post_metal = models.IntegerField(db_column='post metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    post_punk = models.IntegerField(db_column='post punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    post_rock = models.IntegerField(db_column='post rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    post_screamo = models.IntegerField(db_column='post screamo', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    power_electronics = models.IntegerField(db_column='power electronics', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    power_metal = models.IntegerField(db_column='power metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    power_pop = models.IntegerField(db_column='power pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    power_pop_punk = models.IntegerField(db_column='power pop punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    power_thrash = models.IntegerField(db_column='power thrash', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    powerviolence = models.IntegerField(blank=True, null=True)
    praise = models.IntegerField(blank=True, null=True)
    prog_metal = models.IntegerField(db_column='prog metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    progressive_black_metal = models.IntegerField(db_column='progressive black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    progressive_death_metal = models.IntegerField(db_column='progressive death metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    progressive_deathcore = models.IntegerField(db_column='progressive deathcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    progressive_doom = models.IntegerField(db_column='progressive doom', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    progressive_electro_house = models.IntegerField(db_column='progressive electro house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    progressive_groove_metal = models.IntegerField(db_column='progressive groove metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    progressive_house = models.IntegerField(db_column='progressive house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    progressive_metal = models.IntegerField(db_column='progressive metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    progressive_metalcore = models.IntegerField(db_column='progressive metalcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    progressive_post_hardcore = models.IntegerField(db_column='progressive post hardcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    progressive_power_metal = models.IntegerField(db_column='progressive power metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    progressive_psytrance = models.IntegerField(db_column='progressive psytrance', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    progressive_rock = models.IntegerField(db_column='progressive rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    progressive_technical_death_metal = models.IntegerField(db_column='progressive technical death metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    progressive_thrash = models.IntegerField(db_column='progressive thrash', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    progressive_trance = models.IntegerField(db_column='progressive trance', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    protopunk = models.IntegerField(blank=True, null=True)
    psychedelic_doom = models.IntegerField(db_column='psychedelic doom', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    psychedelic_folk = models.IntegerField(db_column='psychedelic folk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    psychedelic_pop = models.IntegerField(db_column='psychedelic pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    psychedelic_rock = models.IntegerField(db_column='psychedelic rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    psychedelic_soul = models.IntegerField(db_column='psychedelic soul', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    psychedelic_trance = models.IntegerField(db_column='psychedelic trance', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    psychill = models.IntegerField(blank=True, null=True)
    psychobilly = models.IntegerField(blank=True, null=True)
    pub_rock = models.IntegerField(db_column='pub rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    punk = models.IntegerField(blank=True, null=True)
    punk_blues = models.IntegerField(db_column='punk blues', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    punk_n_roll = models.IntegerField(db_column='punk n roll', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    punk_ska = models.IntegerField(db_column='punk ska', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    queercore = models.IntegerField(blank=True, null=True)
    quiet_storm = models.IntegerField(db_column='quiet storm', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    quran = models.IntegerField(blank=True, null=True)
    r_b = models.IntegerField(db_column='r b', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    rai = models.IntegerField(blank=True, null=True)
    rain = models.IntegerField(blank=True, null=True)
    ranchera = models.IntegerField(blank=True, null=True)
    rap = models.IntegerField(blank=True, null=True)
    rap_metal = models.IntegerField(db_column='rap metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    rap_rock = models.IntegerField(db_column='rap rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    rare_groove = models.IntegerField(db_column='rare groove', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    rave = models.IntegerField(blank=True, null=True)
    raw_black_metal = models.IntegerField(db_column='raw black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    reading = models.IntegerField(blank=True, null=True)
    redneck = models.IntegerField(blank=True, null=True)
    reggae = models.IntegerField(blank=True, null=True)
    reggae_fusion = models.IntegerField(db_column='reggae fusion', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    reggae_rock = models.IntegerField(db_column='reggae rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    reggaeton = models.IntegerField(blank=True, null=True)
    regional_mexican = models.IntegerField(db_column='regional mexican', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    renaissance = models.IntegerField(blank=True, null=True)
    retro_metal = models.IntegerField(db_column='retro metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    retro_soul = models.IntegerField(db_column='retro soul', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    rhythm_and_blues = models.IntegerField(db_column='rhythm and blues', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    riddim = models.IntegerField(blank=True, null=True)
    ringtone = models.IntegerField(blank=True, null=True)
    riot_grrrl = models.IntegerField(db_column='riot grrrl', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ritual_ambient = models.IntegerField(db_column='ritual ambient', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    rock = models.IntegerField(blank=True, null=True)
    rock_and_roll = models.IntegerField(db_column='rock and roll', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    rock_en_espanol = models.IntegerField(db_column='rock en espanol', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    rock_gaucho = models.IntegerField(db_column='rock gaucho', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    rock_nacional = models.IntegerField(db_column='rock nacional', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    rock_steady = models.IntegerField(db_column='rock steady', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    rock_uruguayo = models.IntegerField(db_column='rock uruguayo', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    rockabilly = models.IntegerField(blank=True, null=True)
    romantico = models.IntegerField(blank=True, null=True)
    roots_reggae = models.IntegerField(db_column='roots reggae', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    roots_rock = models.IntegerField(db_column='roots rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    rumba = models.IntegerField(blank=True, null=True)
    salsa = models.IntegerField(blank=True, null=True)
    samba = models.IntegerField(blank=True, null=True)
    samba_jazz = models.IntegerField(db_column='samba jazz', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    samba_reggae = models.IntegerField(db_column='samba reggae', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    samba_rock = models.IntegerField(db_column='samba rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    schlager = models.IntegerField(blank=True, null=True)
    scottish_folk = models.IntegerField(db_column='scottish folk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    scratch = models.IntegerField(blank=True, null=True)
    screamo = models.IntegerField(blank=True, null=True)
    screamocore = models.IntegerField(blank=True, null=True)
    sertanejo = models.IntegerField(blank=True, null=True)
    sertanejo_universitario = models.IntegerField(db_column='sertanejo universitario', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    shamanic = models.IntegerField(blank=True, null=True)
    shanty = models.IntegerField(blank=True, null=True)
    shoegaze = models.IntegerField(blank=True, null=True)
    show_tunes = models.IntegerField(db_column='show tunes', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    shred = models.IntegerField(blank=True, null=True)
    singer_songwriter = models.IntegerField(db_column='singer songwriter', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sitar = models.IntegerField(blank=True, null=True)
    ska = models.IntegerField(blank=True, null=True)
    ska_punk = models.IntegerField(db_column='ska punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ska_revival = models.IntegerField(db_column='ska revival', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    skate_punk = models.IntegerField(db_column='skate punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    skiffle = models.IntegerField(blank=True, null=True)
    skramz = models.IntegerField(blank=True, null=True)
    slam_death_metal = models.IntegerField(db_column='slam death metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    slayer = models.IntegerField(blank=True, null=True)
    sleaze_rock = models.IntegerField(db_column='sleaze rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sleep = models.IntegerField(blank=True, null=True)
    slowcore = models.IntegerField(blank=True, null=True)
    sludge_metal = models.IntegerField(db_column='sludge metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sludgecore = models.IntegerField(blank=True, null=True)
    smooth_jazz = models.IntegerField(db_column='smooth jazz', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    smooth_soul = models.IntegerField(db_column='smooth soul', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    soft_rock = models.IntegerField(db_column='soft rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sophisti_pop = models.IntegerField(db_column='sophisti pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    soul = models.IntegerField(blank=True, null=True)
    soul_blues = models.IntegerField(db_column='soul blues', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    soul_jazz = models.IntegerField(db_column='soul jazz', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    soulful_house = models.IntegerField(db_column='soulful house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sound = models.IntegerField(blank=True, null=True)
    sound_collage = models.IntegerField(db_column='sound collage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    soundtrack = models.IntegerField(blank=True, null=True)
    southern_hip_hop = models.IntegerField(db_column='southern hip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    southern_metal = models.IntegerField(db_column='southern metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    southern_rock = models.IntegerField(db_column='southern rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    southern_soul = models.IntegerField(db_column='southern soul', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    space_age_pop = models.IntegerField(db_column='space age pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    space_ambient = models.IntegerField(db_column='space ambient', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    space_rock = models.IntegerField(db_column='space rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    spanish_pop = models.IntegerField(db_column='spanish pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    spanish_rock = models.IntegerField(db_column='spanish rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    speed_metal = models.IntegerField(db_column='speed metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    speedcore = models.IntegerField(blank=True, null=True)
    spoken_word = models.IntegerField(db_column='spoken word', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    steampunk = models.IntegerField(blank=True, null=True)
    steel_guitar = models.IntegerField(db_column='steel guitar', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stoner_metal = models.IntegerField(db_column='stoner metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stoner_rock = models.IntegerField(db_column='stoner rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    straight_edge = models.IntegerField(db_column='straight edge', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    street_punk = models.IntegerField(db_column='street punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sung_poetry = models.IntegerField(db_column='sung poetry', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sunshine_pop = models.IntegerField(db_column='sunshine pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    suomi_rock = models.IntegerField(db_column='suomi rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    suomirap = models.IntegerField(blank=True, null=True)
    supergroup = models.IntegerField(blank=True, null=True)
    surf_music = models.IntegerField(db_column='surf music', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    surf_punk = models.IntegerField(db_column='surf punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    swamp_rock = models.IntegerField(db_column='swamp rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    swancore = models.IntegerField(blank=True, null=True)
    swedish_black_metal = models.IntegerField(db_column='swedish black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    swedish_death_metal = models.IntegerField(db_column='swedish death metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    swedish_emo = models.IntegerField(db_column='swedish emo', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    swedish_garage_rock = models.IntegerField(db_column='swedish garage rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    swedish_indie_pop = models.IntegerField(db_column='swedish indie pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    swedish_metal = models.IntegerField(db_column='swedish metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    swedish_pop = models.IntegerField(db_column='swedish pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    swedish_punk = models.IntegerField(db_column='swedish punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    swing = models.IntegerField(blank=True, null=True)
    swiss_metal = models.IntegerField(db_column='swiss metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    symphonic_black_metal = models.IntegerField(db_column='symphonic black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    symphonic_death_metal = models.IntegerField(db_column='symphonic death metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    symphonic_deathcore = models.IntegerField(db_column='symphonic deathcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    symphonic_melodic_death_metal = models.IntegerField(db_column='symphonic melodic death metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    symphonic_metal = models.IntegerField(db_column='symphonic metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    symphonic_power_metal = models.IntegerField(db_column='symphonic power metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    symphonic_rock = models.IntegerField(db_column='symphonic rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    synth_funk = models.IntegerField(db_column='synth funk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    synth_punk = models.IntegerField(db_column='synth punk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    synthesizer = models.IntegerField(blank=True, null=True)
    synthpop = models.IntegerField(blank=True, null=True)
    synthwave = models.IntegerField(blank=True, null=True)
    szanty = models.IntegerField(blank=True, null=True)
    talent_show = models.IntegerField(db_column='talent show', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tango = models.IntegerField(blank=True, null=True)
    tarantella = models.IntegerField(blank=True, null=True)
    tech_house = models.IntegerField(db_column='tech house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    technical_black_metal = models.IntegerField(db_column='technical black metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    technical_brutal_death_metal = models.IntegerField(db_column='technical brutal death metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    technical_death_metal = models.IntegerField(db_column='technical death metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    technical_deathcore = models.IntegerField(db_column='technical deathcore', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    technical_groove_metal = models.IntegerField(db_column='technical groove metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    technical_melodic_death_metal = models.IntegerField(db_column='technical melodic death metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    techno = models.IntegerField(blank=True, null=True)
    tecnobrega = models.IntegerField(blank=True, null=True)
    teen_pop = models.IntegerField(db_column='teen pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tejano = models.IntegerField(blank=True, null=True)
    texas_blues = models.IntegerField(db_column='texas blues', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    texas_country = models.IntegerField(db_column='texas country', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    texas_metal = models.IntegerField(db_column='texas metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    theme = models.IntegerField(blank=True, null=True)
    therapy = models.IntegerField(blank=True, null=True)
    theremin = models.IntegerField(blank=True, null=True)
    thrash_groove_metal = models.IntegerField(db_column='thrash groove metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    thrash_metal = models.IntegerField(db_column='thrash metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    throat_singing = models.IntegerField(db_column='throat singing', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tolkien_metal = models.IntegerField(db_column='tolkien metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    traditional_country = models.IntegerField(db_column='traditional country', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    traditional_folk = models.IntegerField(db_column='traditional folk', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    trance = models.IntegerField(blank=True, null=True)
    trancecore = models.IntegerField(blank=True, null=True)
    trap = models.IntegerField(blank=True, null=True)
    trash_rock = models.IntegerField(db_column='trash rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tribal_house = models.IntegerField(db_column='tribal house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tribute = models.IntegerField(blank=True, null=True)
    trip_hop = models.IntegerField(db_column='trip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tropical = models.IntegerField(blank=True, null=True)
    tropical_house = models.IntegerField(db_column='tropical house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tropicalia = models.IntegerField(blank=True, null=True)
    trova = models.IntegerField(blank=True, null=True)
    tuna = models.IntegerField(blank=True, null=True)
    turntablism = models.IntegerField(blank=True, null=True)
    twee_pop = models.IntegerField(db_column='twee pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    uk_funky = models.IntegerField(db_column='uk funky', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    uk_garage = models.IntegerField(db_column='uk garage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    uk_hip_hop = models.IntegerField(db_column='uk hip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    uk_pop = models.IntegerField(db_column='uk pop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ukulele = models.IntegerField(blank=True, null=True)
    underground_hip_hop = models.IntegerField(db_column='underground hip hop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    underground_rap = models.IntegerField(db_column='underground rap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    uplifting_trance = models.IntegerField(db_column='uplifting trance', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    urban_contemporary = models.IntegerField(db_column='urban contemporary', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    us_power_metal = models.IntegerField(db_column='us power metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    usbm = models.IntegerField(blank=True, null=True)
    vaudeville = models.IntegerField(blank=True, null=True)
    velha_guarda = models.IntegerField(db_column='velha guarda', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    video_game_music = models.IntegerField(db_column='video game music', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    viking_metal = models.IntegerField(db_column='viking metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    violin = models.IntegerField(blank=True, null=True)
    visual_kei = models.IntegerField(db_column='visual kei', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    vocal_house = models.IntegerField(db_column='vocal house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    vocal_jazz = models.IntegerField(db_column='vocal jazz', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    vocal_trance = models.IntegerField(db_column='vocal trance', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    vogue = models.IntegerField(blank=True, null=True)
    war_metal = models.IntegerField(db_column='war metal', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    water = models.IntegerField(blank=True, null=True)
    wave = models.IntegerField(blank=True, null=True)
    west_coast_rap = models.IntegerField(db_column='west coast rap', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    western_swing = models.IntegerField(db_column='western swing', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    white_noise = models.IntegerField(db_column='white noise', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    witch_house = models.IntegerField(db_column='witch house', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    world = models.IntegerField(blank=True, null=True)
    world_fusion = models.IntegerField(db_column='world fusion', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    worship = models.IntegerField(blank=True, null=True)
    wrestling = models.IntegerField(blank=True, null=True)
    yacht_rock = models.IntegerField(db_column='yacht rock', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ye_ye = models.IntegerField(db_column='ye ye', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    zen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'songs'
