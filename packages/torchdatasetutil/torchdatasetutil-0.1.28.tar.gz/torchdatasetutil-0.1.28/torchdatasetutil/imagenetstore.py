import sys
import os
from pycocotools import mask
import numpy as np
import cv2
import json
import functools
from collections import defaultdict
import torch
from tqdm import tqdm
from torch.utils.data import Dataset
import torchvision
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

from pymlutil.s3 import s3store, Connect
from pymlutil.jsonutil import ReadDict
from pymlutil.imutil import ImUtil, ImTransform, AddGaussianNoise, ResizePad
from torch.utils.data.dataloader import default_collate
from torchvision.transforms.functional import InterpolationMode

sys.path.insert(0, os.path.abspath(''))
import torchdatasetutil.mixuptransforms
from torchdatasetutil.sampler import RASampler

ImagenetClasses = ['tench, Tinca tinca',
'goldfish, Carassius auratus',
'great white shark, white shark, man-eater, man-eating shark, Carcharodon caharias',
'tiger shark, Galeocerdo cuvieri',
'hammerhead, hammerhead shark',
'electric ray, crampfish, numbfish, torpedo',
'stingray',
'cock',
'hen',
'ostrich, Struthio camelus',
'brambling, Fringilla montifringilla',
'goldfinch, Carduelis carduelis',
'house finch, linnet, Carpodacus mexicanus',
'junco, snowbird',
'indigo bunting, indigo finch, indigo bird, Passerina cyanea',
'robin, American robin, Turdus migratorius',
'bulbul',
'jay',
'magpie',
'chickadee',
'water ouzel, dipper',
'kite',
'bald eagle, American eagle, Haliaeetus leucocephalus',
'vulture',
'great grey owl, great gray owl, Strix nebulosa',
'European fire salamander, Salamandra salamandra',
'common newt, Triturus vulgaris',
'eft',
'spotted salamander, Ambystoma maculatum',
'axolotl, mud puppy, Ambystoma mexicanum',
'bullfrog, Rana catesbeiana',
'tree frog, tree-frog',
'tailed frog, bell toad, ribbed toad, tailed toad, Ascaphus trui',
'loggerhead, loggerhead turtle, Caretta caretta',
'leatherback turtle, leatherback, leathery turtle, Dermochelys coriacea',
'mud turtle',
'terrapin',
'box turtle, box tortoise',
'banded gecko',
'common iguana, iguana, Iguana iguana',
'American chameleon, anole, Anolis carolinensis',
'whiptail, whiptail lizard',
'agama',
'frilled lizard, Chlamydosaurus kingi',
'alligator lizard',
'Gila monster, Heloderma suspectum',
'green lizard, Lacerta viridis',
'African chameleon, Chamaeleo chamaeleon',
'Komodo dragon, Komodo lizard, dragon lizard, giant lizard, Varanus komodoeis',
'African crocodile, Nile crocodile, Crocodylus niloticus',
'American alligator, Alligator mississipiensis',
'triceratops',
'thunder snake, worm snake, Carphophis amoenus',
'ringneck snake, ring-necked snake, ring snake',
'hognose snake, puff adder, sand viper',
'green snake, grass snake',
'king snake, kingsnake',
'garter snake, grass snake',
'water snake',
'vine snake',
'night snake, Hypsiglena torquata',
'boa constrictor, Constrictor constrictor',
'rock python, rock snake, Python sebae',
'Indian cobra, Naja naja',
'green mamba',
'sea snake',
'horned viper, cerastes, sand viper, horned asp, Cerastes cornutus',
'diamondback, diamondback rattlesnake, Crotalus adamanteus',
'sidewinder, horned rattlesnake, Crotalus cerastes',
'trilobite',
'harvestman, daddy longlegs, Phalangium opilio',
'scorpion',
'black and gold garden spider, Argiope aurantia',
'barn spider, Araneus cavaticus',
'garden spider, Aranea diademata',
'black widow, Latrodectus mactans',
'tarantula',
'wolf spider, hunting spider',
'tick',
'centipede',
'black grouse',
'ptarmigan',
'ruffed grouse, partridge, Bonasa umbellus',
'prairie chicken, prairie grouse, prairie fowl',
'peacock',
'quail',
'partridge',
'African grey, African gray, Psittacus erithacus',
'macaw',
'sulphur-crested cockatoo, Kakatoe galerita, Cacatua galerita',
'lorikeet',
'coucal',
'bee eater',
'hornbill',
'hummingbird',
'jacamar',
'toucan',
'drake',
'red-breasted merganser, Mergus serrator',
'goose',
'black swan, Cygnus atratus',
'tusker',
'echidna, spiny anteater, anteater',
'platypus, duckbill, duckbilled platypus, duck-billed platypus, Ornithorhyhus anatinus',
'wallaby, brush kangaroo',
'koala, koala bear, kangaroo bear, native bear, Phascolarctos cinereus',
'wombat',
'jellyfish',
'sea anemone, anemone',
'brain coral',
'flatworm, platyhelminth',
'nematode, nematode worm, roundworm',
'conch',
'snail',
'slug',
'sea slug, nudibranch',
'chiton, coat-of-mail shell, sea cradle, polyplacophore',
'chambered nautilus, pearly nautilus, nautilus',
'Dungeness crab, Cancer magister',
'rock crab, Cancer irroratus',
'fiddler crab',
'king crab, Alaska crab, Alaskan king crab, Alaska king crab, Paralithodesamtschatica',
'American lobster, Northern lobster, Maine lobster, Homarus americanus',
'spiny lobster, langouste, rock lobster, crawfish, crayfish, sea crawfish',
'crayfish, crawfish, crawdad, crawdaddy',
'hermit crab',
'isopod',
'white stork, Ciconia ciconia',
'black stork, Ciconia nigra',
'spoonbill',
'flamingo',
'little blue heron, Egretta caerulea',
'American egret, great white heron, Egretta albus',
'bittern',
'crane, bird',
'limpkin, Aramus pictus',
'European gallinule, Porphyrio porphyrio',
'American coot, marsh hen, mud hen, water hen, Fulica americana',
'bustard',
'ruddy turnstone, Arenaria interpres',
'red-backed sandpiper, dunlin, Erolia alpina',
'redshank, Tringa totanus',
'dowitcher',
'oystercatcher, oyster catcher',
'pelican',
'king penguin, Aptenodytes patagonica',
'albatross, mollymawk',
'grey whale, gray whale, devilfish, Eschrichtius gibbosus, Eschrichtius rostus',
'killer whale, killer, orca, grampus, sea wolf, Orcinus orca',
'dugong, Dugong dugon',
'sea lion',
'Chihuahua',
'Japanese spaniel',
'Maltese dog, Maltese terrier, Maltese',
'Pekinese, Pekingese, Peke',
'Shih-Tzu',
'Blenheim spaniel',
'papillon',
'toy terrier',
'Rhodesian ridgeback',
'Afghan hound, Afghan',
'basset, basset hound',
'beagle',
'bloodhound, sleuthhound',
'bluetick',
'black-and-tan coonhound',
'Walker hound, Walker foxhound',
'English foxhound',
'redbone',
'borzoi, Russian wolfhound',
'Irish wolfhound',
'Italian greyhound',
'whippet',
'Ibizan hound, Ibizan Podenco',
'Norwegian elkhound, elkhound',
'otterhound, otter hound',
'Saluki, gazelle hound',
'Scottish deerhound, deerhound',
'Weimaraner',
'Staffordshire bullterrier, Staffordshire bull terrier',
'American Staffordshire terrier, Staffordshire terrier, American pit bull rrier, pit bull terrier',
'Bedlington terrier',
'Border terrier',
'Kerry blue terrier',
'Irish terrier',
'Norfolk terrier',
'Norwich terrier',
'Yorkshire terrier',
'wire-haired fox terrier',
'Lakeland terrier',
'Sealyham terrier, Sealyham',
'Airedale, Airedale terrier',
'cairn, cairn terrier',
'Australian terrier',
'Dandie Dinmont, Dandie Dinmont terrier',
'Boston bull, Boston terrier',
'miniature schnauzer',
'giant schnauzer',
'standard schnauzer',
'Scotch terrier, Scottish terrier, Scottie',
'Tibetan terrier, chrysanthemum dog',
'silky terrier, Sydney silky',
'soft-coated wheaten terrier',
'West Highland white terrier',
'Lhasa, Lhasa apso',
'flat-coated retriever',
'curly-coated retriever',
'golden retriever',
'Labrador retriever',
'Chesapeake Bay retriever',
'German short-haired pointer',
'vizsla, Hungarian pointer',
'English setter',
'Irish setter, red setter',
'Gordon setter',
'Brittany spaniel',
'clumber, clumber spaniel',
'English springer, English springer spaniel',
'Welsh springer spaniel',
'cocker spaniel, English cocker spaniel, cocker',
'Sussex spaniel',
'Irish water spaniel',
'kuvasz',
'schipperke',
'groenendael',
'malinois',
'briard',
'kelpie',
'komondor',
'Old English sheepdog, bobtail',
'Shetland sheepdog, Shetland sheep dog, Shetland',
'collie',
'Border collie',
'Bouvier des Flandres, Bouviers des Flandres',
'Rottweiler',
'German shepherd, German shepherd dog, German police dog, alsatian',
'Doberman, Doberman pinscher',
'miniature pinscher',
'Greater Swiss Mountain dog',
'Bernese mountain dog',
'Appenzeller',
'EntleBucher',
'boxer',
'bull mastiff',
'Tibetan mastiff',
'French bulldog',
'Great Dane',
'Saint Bernard, St Bernard',
'Eskimo dog, husky',
'malamute, malemute, Alaskan malamute',
'Siberian husky',
'dalmatian, coach dog, carriage dog',
'affenpinscher, monkey pinscher, monkey dog',
'basenji',
'pug, pug-dog',
'Leonberg',
'Newfoundland, Newfoundland dog',
'Great Pyrenees',
'Samoyed, Samoyede',
'Pomeranian',
'chow, chow chow',
'keeshond',
'Brabancon griffon',
'Pembroke, Pembroke Welsh corgi',
'Cardigan, Cardigan Welsh corgi',
'toy poodle',
'miniature poodle',
'standard poodle',
'Mexican hairless',
'timber wolf, grey wolf, gray wolf, Canis lupus',
'white wolf, Arctic wolf, Canis lupus tundrarum',
'red wolf, maned wolf, Canis rufus, Canis niger',
'coyote, prairie wolf, brush wolf, Canis latrans',
'dingo, warrigal, warragal, Canis dingo',
'dhole, Cuon alpinus',
'African hunting dog, hyena dog, Cape hunting dog, Lycaon pictus',
'hyena, hyaena',
'red fox, Vulpes vulpes',
'kit fox, Vulpes macrotis',
'Arctic fox, white fox, Alopex lagopus',
'grey fox, gray fox, Urocyon cinereoargenteus',
'tabby, tabby cat',
'tiger cat',
'Persian cat',
'Siamese cat, Siamese',
'Egyptian cat',
'cougar, puma, catamount, mountain lion, painter, panther, Felis concolor',
'lynx, catamount',
'leopard, Panthera pardus',
'snow leopard, ounce, Panthera uncia',
'jaguar, panther, Panthera onca, Felis onca',
'lion, king of beasts, Panthera leo',
'tiger, Panthera tigris',
'cheetah, chetah, Acinonyx jubatus',
'brown bear, bruin, Ursus arctos',
'American black bear, black bear, Ursus americanus, Euarctos americanus',
'ice bear, polar bear, Ursus Maritimus, Thalarctos maritimus',
'sloth bear, Melursus ursinus, Ursus ursinus',
'mongoose',
'meerkat, mierkat',
'tiger beetle',
'ladybug, ladybeetle, lady beetle, ladybird, ladybird beetle',
'ground beetle, carabid beetle',
'long-horned beetle, longicorn, longicorn beetle',
'leaf beetle, chrysomelid',
'dung beetle',
'rhinoceros beetle',
'weevil',
'fly',
'bee',
'ant, emmet, pismire',
'grasshopper, hopper',
'cricket',
'walking stick, walkingstick, stick insect',
'cockroach, roach',
'mantis, mantid',
'cicada, cicala',
'leafhopper',
'lacewing, lacewing fly',
'dragonfly, darning needle, devil\'s darning needle, sewing needle, snake fder, snake doctor, mosquito hawk, skeeter hawk',
'damselfly',
'admiral',
'ringlet, ringlet butterfly',
'monarch, monarch butterfly, milkweed butterfly, Danaus plexippus',
'cabbage butterfly',
'sulphur butterfly, sulfur butterfly',
'lycaenid, lycaenid butterfly',
'starfish, sea star',
'sea urchin',
'sea cucumber, holothurian',
'wood rabbit, cottontail, cottontail rabbit',
'hare',
'Angora, Angora rabbit',
'hamster',
'porcupine, hedgehog',
'fox squirrel, eastern fox squirrel, Sciurus niger',
'marmot',
'beaver',
'guinea pig, Cavia cobaya',
'sorrel',
'zebra',
'hog, pig, grunter, squealer, Sus scrofa',
'wild boar, boar, Sus scrofa',
'warthog',
'hippopotamus, hippo, river horse, Hippopotamus amphibius',
'ox',
'water buffalo, water ox, Asiatic buffalo, Bubalus bubalis',
'bison',
'ram, tup',
'bighorn, bighorn sheep, cimarron, Rocky Mountain bighorn, Rocky Mountain eep, Ovis canadensis',
'ibex, Capra ibex',
'hartebeest',
'impala, Aepyceros melampus',
'gazelle',
'Arabian camel, dromedary, Camelus dromedarius',
'llama',
'weasel',
'mink',
'polecat, fitch, foulmart, foumart, Mustela putorius',
'black-footed ferret, ferret, Mustela nigripes',
'otter',
'skunk, polecat, wood pussy',
'badger',
'armadillo',
'three-toed sloth, ai, Bradypus tridactylus',
'orangutan, orang, orangutang, Pongo pygmaeus',
'gorilla, Gorilla gorilla',
'chimpanzee, chimp, Pan troglodytes',
'gibbon, Hylobates lar',
'siamang, Hylobates syndactylus, Symphalangus syndactylus',
'guenon, guenon monkey',
'patas, hussar monkey, Erythrocebus patas',
'baboon',
'macaque',
'langur',
'colobus, colobus monkey',
'proboscis monkey, Nasalis larvatus',
'marmoset',
'capuchin, ringtail, Cebus capucinus',
'howler monkey, howler',
'titi, titi monkey',
'spider monkey, Ateles geoffroyi',
'squirrel monkey, Saimiri sciureus',
'Madagascar cat, ring-tailed lemur, Lemur catta',
'indri, indris, Indri indri, Indri brevicaudatus',
'Indian elephant, Elephas maximus',
'African elephant, Loxodonta africana',
'lesser panda, red panda, panda, bear cat, cat bear, Ailurus fulgens',
'giant panda, panda, panda bear, coon bear, Ailuropoda melanoleuca',
'barracouta, snoek',
'eel',
'coho, cohoe, coho salmon, blue jack, silver salmon, Oncorhynchus kisutch',
'rock beauty, Holocanthus tricolor',
'anemone fish',
'sturgeon',
'gar, garfish, garpike, billfish, Lepisosteus osseus',
'lionfish',
'puffer, pufferfish, blowfish, globefish',
'abacus',
'abaya',
'academic gown, academic robe, judge\'s robe',
'accordion, piano accordion, squeeze box',
'acoustic guitar',
'aircraft carrier, carrier, flattop, attack aircraft carrier',
'airliner',
'airship, dirigible',
'altar',
'ambulance',
'amphibian, amphibious vehicle',
'analog clock',
'apiary, bee house',
'apron',
'ashcan, trash can, garbage can, wastebin, ash bin, ash-bin, ashbin, dustb, trash barrel, trash bin',
'assault rifle, assault gun',
'backpack, back pack, knapsack, packsack, rucksack, haversack',
'bakery, bakeshop, bakehouse',
'balance beam, beam',
'balloon',
'ballpoint, ballpoint pen, ballpen, Biro',
'Band Aid',
'banjo',
'bannister, banister, balustrade, balusters, handrail',
'barbell',
'barber chair',
'barbershop',
'barn',
'barometer',
'barrel, cask',
'barrow, garden cart, lawn cart, wheelbarrow',
'baseball',
'basketball',
'bassinet',
'bassoon',
'bathing cap, swimming cap',
'bath towel',
'bathtub, bathing tub, bath, tub',
'beach wagon, station wagon, wagon, estate car, beach waggon, station wagg, waggon',
'beacon, lighthouse, beacon light, pharos',
'beaker',
'bearskin, busby, shako',
'beer bottle',
'beer glass',
'bell cote, bell cot',
'bib',
'bicycle-built-for-two, tandem bicycle, tandem',
'bikini, two-piece',
'binder, ring-binder',
'binoculars, field glasses, opera glasses',
'birdhouse',
'boathouse',
'bobsled, bobsleigh, bob',
'bolo tie, bolo, bola tie, bola',
'bonnet, poke bonnet',
'bookcase',
'bookshop, bookstore, bookstall',
'bottlecap',
'bow',
'bow tie, bow-tie, bowtie',
'brass, memorial tablet, plaque',
'brassiere, bra, bandeau',
'breakwater, groin, groyne, mole, bulwark, seawall, jetty',
'breastplate, aegis, egis',
'broom',
'bucket, pail',
'buckle',
'bulletproof vest',
'bullet train, bullet',
'butcher shop, meat market',
'cab, hack, taxi, taxicab',
'caldron, cauldron',
'candle, taper, wax light',
'cannon',
'canoe',
'can opener, tin opener',
'cardigan',
'car mirror',
'carousel, carrousel, merry-go-round, roundabout, whirligig',
'carpenter\'s kit, tool kit',
'carton',
'car wheel',
'cash machine, cash dispenser, automated teller machine, automatic teller chine, automated teller, automatic teller, ATM',
'cassette',
'cassette player',
'castle',
'catamaran',
'CD player',
'cello, violoncello',
'cellular telephone, cellular phone, cellphone, cell, mobile phone',
'chain',
'chainlink fence',
'chain mail, ring mail, mail, chain armor, chain armour, ring armor, ring mour',
'chain saw, chainsaw',
'chest',
'chiffonier, commode',
'chime, bell, gong',
'china cabinet, china closet',
'Christmas stocking',
'church, church building',
'cinema, movie theater, movie theatre, movie house, picture palace',
'cleaver, meat cleaver, chopper',
'cliff dwelling',
'cloak',
'clog, geta, patten, sabot',
'cocktail shaker',
'coffee mug',
'coffeepot',
'coil, spiral, volute, whorl, helix',
'combination lock',
'computer keyboard, keypad',
'confectionery, confectionary, candy store',
'container ship, containership, container vessel',
'convertible',
'corkscrew, bottle screw',
'cornet, horn, trumpet, trump',
'cowboy boot',
'cowboy hat, ten-gallon hat',
'cradle',
'crane',
'crash helmet',
'crate',
'crib, cot',
'Crock Pot',
'croquet ball',
'crutch',
'cuirass',
'dam, dike, dyke',
'desk',
'desktop computer',
'dial telephone, dial phone',
'diaper, nappy, napkin',
'digital clock',
'digital watch',
'dining table, board',
'dishrag, dishcloth',
'dishwasher, dish washer, dishwashing machine',
'disk brake, disc brake',
'dock, dockage, docking facility',
'dogsled, dog sled, dog sleigh',
'dome',
'doormat, welcome mat',
'drilling platform, offshore rig',
'drum, membranophone, tympan',
'drumstick',
'dumbbell',
'Dutch oven',
'electric fan, blower',
'electric guitar',
'electric locomotive',
'entertainment center',
'envelope',
'espresso maker',
'face powder',
'feather boa, boa',
'file, file cabinet, filing cabinet',
'fireboat',
'fire engine, fire truck',
'fire screen, fireguard',
'flagpole, flagstaff',
'flute, transverse flute',
'folding chair',
'football helmet',
'forklift',
'fountain',
'fountain pen',
'four-poster',
'freight car',
'French horn, horn',
'frying pan, frypan, skillet',
'fur coat',
'garbage truck, dustcart',
'gasmask, respirator, gas helmet',
'gas pump, gasoline pump, petrol pump, island dispenser',
'goblet',
'go-kart',
'golf ball',
'golfcart, golf cart',
'gondola',
'gong, tam-tam',
'gown',
'grand piano, grand',
'greenhouse, nursery, glasshouse',
'grille, radiator grille',
'grocery store, grocery, food market, market',
'guillotine',
'hair slide',
'hair spray',
'half track',
'hammer',
'hamper',
'hand blower, blow dryer, blow drier, hair dryer, hair drier',
'hand-held computer, hand-held microcomputer',
'handkerchief, hankie, hanky, hankey',
'hard disc, hard disk, fixed disk',
'harmonica, mouth organ, harp, mouth harp',
'harp',
'harvester, reaper',
'hatchet',
'holster',
'home theater, home theatre',
'honeycomb',
'hook, claw',
'hoopskirt, crinoline',
'horizontal bar, high bar',
'horse cart, horse-cart',
'hourglass',
'iPod',
'iron, smoothing iron',
'jack-o\'-lantern',
'jean, blue jean, denim',
'jeep, landrover',
'jersey, T-shirt, tee shirt',
'jigsaw puzzle',
'jinrikisha, ricksha, rickshaw',
'joystick',
'kimono',
'knee pad',
'knot',
'lab coat, laboratory coat',
'ladle',
'lampshade, lamp shade',
'laptop, laptop computer',
'lawn mower, mower',
'lens cap, lens cover',
'letter opener, paper knife, paperknife',
'library',
'lifeboat',
'lighter, light, igniter, ignitor',
'limousine, limo',
'liner, ocean liner',
'lipstick, lip rouge',
'Loafer',
'lotion',
'loudspeaker, speaker, speaker unit, loudspeaker system, speaker system',
'loupe, jeweler\'s loupe',
'lumbermill, sawmill',
'magnetic compass',
'mailbag, postbag',
'mailbox, letter box',
'maillot',
'maillot, tank suit',
'manhole cover',
'maraca',
'marimba, xylophone',
'mask',
'matchstick',
'maypole',
'maze, labyrinth',
'measuring cup',
'medicine chest, medicine cabinet',
'megalith, megalithic structure',
'microphone, mike',
'microwave, microwave oven',
'military uniform',
'milk can',
'minibus',
'miniskirt, mini',
'minivan',
'missile',
'mitten',
'mixing bowl',
'mobile home, manufactured home',
'Model T',
'modem',
'monastery',
'monitor',
'moped',
'mortar',
'mortarboard',
'mosque',
'mosquito net',
'motor scooter, scooter',
'mountain bike, all-terrain bike, off-roader',
'mountain tent',
'mouse, computer mouse',
'mousetrap',
'moving van',
'muzzle',
'nail',
'neck brace',
'necklace',
'nipple',
'notebook, notebook computer',
'obelisk',
'oboe, hautboy, hautbois',
'ocarina, sweet potato',
'odometer, hodometer, mileometer, milometer',
'oil filter',
'organ, pipe organ',
'oscilloscope, scope, cathode-ray oscilloscope, CRO',
'overskirt',
'oxcart',
'oxygen mask',
'packet',
'paddle, boat paddle',
'paddlewheel, paddle wheel',
'padlock',
'paintbrush',
'pajama, pyjama, pj\'s, jammies',
'palace',
'panpipe, pandean pipe, syrinx',
'paper towel',
'parachute, chute',
'parallel bars, bars',
'park bench',
'parking meter',
'passenger car, coach, carriage',
'patio, terrace',
'pay-phone, pay-station',
'pedestal, plinth, footstall',
'pencil box, pencil case',
'pencil sharpener',
'perfume, essence',
'Petri dish',
'photocopier',
'pick, plectrum, plectron',
'pickelhaube',
'picket fence, paling',
'pickup, pickup truck',
'pier',
'piggy bank, penny bank',
'pill bottle',
'pillow',
'ping-pong ball',
'pinwheel',
'pirate, pirate ship',
'pitcher, ewer',
'plane, carpenter\'s plane, woodworking plane',
'planetarium',
'plastic bag',
'plate rack',
'plow, plough',
'plunger, plumber\'s helper',
'Polaroid camera, Polaroid Land camera',
'pole',
'police van, police wagon, paddy wagon, patrol wagon, wagon, black Maria',
'poncho',
'pool table, billiard table, snooker table',
'pop bottle, soda bottle',
'pot, flowerpot',
'potter\'s wheel',
'power drill',
'prayer rug, prayer mat',
'printer',
'prison, prison house',
'projectile, missile',
'projector',
'puck, hockey puck',
'punching bag, punch bag, punching ball, punchball',
'purse',
'quill, quill pen',
'quilt, comforter, comfort, puff',
'racer, race car, racing car',
'racket, racquet',
'radiator',
'radio, wireless',
'radio telescope, radio reflector',
'rain barrel',
'recreational vehicle, RV, R.V.',
'reel',
'reflex camera',
'refrigerator, icebox',
'remote control, remote',
'restaurant, eating house, eating place, eatery',
'revolver, six-gun, six-shooter',
'rifle',
'rocking chair, rocker',
'rotisserie',
'rubber eraser, rubber, pencil eraser',
'rugby ball',
'rule, ruler',
'running shoe',
'safe',
'safety pin',
'saltshaker, salt shaker',
'sandal',
'sarong',
'sax, saxophone',
'scabbard',
'scale, weighing machine',
'school bus',
'schooner',
'scoreboard',
'screen, CRT screen',
'screw',
'screwdriver',
'seat belt, seatbelt',
'sewing machine',
'shield, buckler',
'shoe shop, shoe-shop, shoe store',
'shoji',
'shopping basket',
'shopping cart',
'shovel',
'shower cap',
'shower curtain',
'ski',
'ski mask',
'sleeping bag',
'slide rule, slipstick',
'sliding door',
'slot, one-armed bandit',
'snorkel',
'snowmobile',
'snowplow, snowplough',
'soap dispenser',
'soccer ball',
'sock',
'solar dish, solar collector, solar furnace',
'sombrero',
'soup bowl',
'space bar',
'space heater',
'space shuttle',
'spatula',
'speedboat',
'spider web, spider\'s web',
'spindle',
'sports car, sport car',
'spotlight, spot',
'stage',
'steam locomotive',
'steel arch bridge',
'steel drum',
'stethoscope',
'stole',
'stone wall',
'stopwatch, stop watch',
'stove',
'strainer',
'streetcar, tram, tramcar, trolley, trolley car',
'stretcher',
'studio couch, day bed',
'stupa, tope',
'submarine, pigboat, sub, U-boat',
'suit, suit of clothes',
'sundial',
'sunglass',
'sunglasses, dark glasses, shades',
'sunscreen, sunblock, sun blocker',
'suspension bridge',
'swab, swob, mop',
'sweatshirt',
'swimming trunks, bathing trunks',
'swing',
'switch, electric switch, electrical switch',
'syringe',
'table lamp',
'tank, army tank, armored combat vehicle, armoured combat vehicle',
'tape player',
'teapot',
'teddy, teddy bear',
'television, television system',
'tennis ball',
'thatch, thatched roof',
'theater curtain, theatre curtain',
'thimble',
'thresher, thrasher, threshing machine',
'throne',
'tile roof',
'toaster',
'tobacco shop, tobacconist shop, tobacconist',
'toilet seat',
'torch',
'totem pole',
'tow truck, tow car, wrecker',
'toyshop',
'tractor',
'trailer truck, tractor trailer, trucking rig, rig, articulated lorry, sem,',
'tray',
'trench coat',
'tricycle, trike, velocipede',
'trimaran',
'tripod',
'triumphal arch',
'trolleybus, trolley coach, trackless trolley',
'trombone',
'tub, vat',
'turnstile',
'typewriter keyboard',
'umbrella',
'unicycle, monocycle',
'upright, upright piano',
'vacuum, vacuum cleaner',
'vase',
'vault',
'velvet',
'vending machine',
'vestment',
'viaduct',
'violin, fiddle',
'volleyball',
'waffle iron',
'wall clock',
'wallet, billfold, notecase, pocketbook',
'wardrobe, closet, press',
'warplane, military plane',
'washbasin, handbasin, washbowl, lavabo, wash-hand basin',
'washer, automatic washer, washing machine',
'water bottle',
'water jug',
'water tower',
'whiskey jug',
'whistle',
'wig',
'window screen',
'window shade',
'Windsor tie',
'wine bottle',
'wing',
'wok',
'wooden spoon',
'wool, woolen, woollen',
'worm fence, snake fence, snake-rail fence, Virginia fence',
'wreck',
'yawl',
'yurt',
'web site, website, internet site, site',
'comic book',
'crossword puzzle, crossword',
'street sign',
'traffic light, traffic signal, stoplight',
'book jacket, dust cover, dust jacket, dust wrapper',
'menu',
'plate',
'guacamole',
'consomme',
'hot pot, hotpot',
'trifle',
'ice cream, icecream',
'ice lolly, lolly, lollipop, popsicle',
'French loaf',
'bagel, beigel',
'pretzel',
'cheeseburger',
'hotdog, hot dog, red hot',
'mashed potato',
'head cabbage',
'broccoli',
'cauliflower',
'zucchini, courgette',
'spaghetti squash',
'acorn squash',
'butternut squash',
'cucumber, cuke',
'artichoke, globe artichoke',
'bell pepper',
'cardoon',
'mushroom',
'Granny Smith',
'strawberry',
'orange',
'lemon',
'fig',
'pineapple, ananas',
'banana',
'jackfruit, jak, jack',
'custard apple',
'pomegranate',
'hay',
'carbonara',
'chocolate sauce, chocolate syrup',
'dough',
'meat loaf, meatloaf',
'pizza, pizza pie',
'potpie',
'burrito',
'red wine',
'espresso',
'cup',
'eggnog',
'alp',
'bubble',
'cliff, drop, drop-off',
'coral reef',
'geyser',
'lakeside, lakeshore',
'promontory, headland, head, foreland',
'sandbar, sand bar',
'seashore, coast, seacoast, sea-coast',
'valley, vale',
'volcano',
'ballplayer, baseball player',
'groom, bridegroom',
'scuba diver',
'rapeseed',
'daisy',
'yellow lady\'s slipper, yellow lady-slipper, Cypripedium calceolus, Cypripium parviflorum',
'corn',
'acorn',
'hip, rose hip, rosehip',
'buckeye, horse chestnut, conker',
'coral fungus',
'agaric',
'gyromitra',
'stinkhorn, carrion fungus',
'earthstar',
'hen-of-the-woods, hen of the woods, Polyporus frondosus, Grifola frondosa',
'bolete',
'ear, spike, capitulum',
'toilet tissue, toilet paper, bathroom tissue']

class Normalize(object):
    """Normalize image.

    Args:
        normalize image mean and standard deviation
    """

    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def __call__(self, sample):
        for i, channel_mean in enumerate(self.mean):
            channel_std = self.std[i]
            imgMean = torch.mean(sample[i])
            imgStd = torch.std(sample[i])
            if imgStd > 0.0:
                sample[i] = (sample[i] - imgMean)/imgStd

            sample[i] = sample[i]*channel_std + channel_mean     

        return sample

def CreateImagenetLoaders(s3, s3def, src, dest, bucket = None, resize_width=224, 
                      resize_height=224, crop_width=256, crop_height=256, batch_size = 2, 
                      num_workers=0, cuda = True, timeout=0, loaders = None, 
                      image_transform=None, label_transform=None, 
                      augment=True, normalize=False, flipX=True, flipY=False, 
                      random_seed = None, numTries=3,
                      rotate=3, scale_min=0.75, scale_max=1.25, offset=0.1, augment_noise=1.0, 
                      normalize_mean = [0.485, 0.456, 0.406], normalize_std=[0.229, 0.224, 0.225], ra_reps=4,
                      mixup_alpha = 0.0, cutmix_alpha=0.0):

    if not bucket:
        bucket = s3def['sets']['dataset']['bucket']

    if not os.path.exists(dest):
        s3.GetDir(bucket, src, dest)

    dest = os.path.join(dest, '') #Ensure there is a trailing slash

    pin_memory = False
    # if cuda:
    #     pin_memory = True


    # Load dataset
    if loaders is None:
        if augment:
            transform_list = []
            transform_list.append(ResizePad(resize_width, resize_height))
            transform_list.append(transforms.RandomHorizontalFlip(p=0.5))
            if rotate > 0 or offset > 0 or scale_min != 1.0 or scale_max != 1.0:
                transform_list.append(transforms.RandomAffine(degrees=rotate,
                        translate=(offset, offset), 
                        scale=(scale_min, scale_max), 
                        interpolation=transforms.InterpolationMode.BILINEAR))
            transform_list.append(transforms.RandomCrop( (crop_width, crop_height), padding=None, pad_if_needed=True, fill=0, padding_mode='constant'))
            transform_list.append(transforms.ToTensor())
            transform_list.append(Normalize(normalize_mean, normalize_std))
            # transform_list.append(transforms.Normalize(
            #     mean=normalize_mean,
            #     std=normalize_std))
            if augment_noise > 0.0:
                transform_list.append(AddGaussianNoise(0., augment_noise))

            train_transform = transforms.Compose(transform_list)

            test_transform = transforms.Compose([
                ResizePad(resize_width, resize_height),
                transforms.CenterCrop( (crop_width, crop_height), padding=None, pad_if_needed=True, fill=0, padding_mode='constant'),
                transforms.ToTensor(),
                Normalize(normalize_mean, normalize_std),
                # transforms.Normalize(
                #     mean=normalize_mean,
                #     std=normalize_std),
            ])

            width = crop_width
            height = crop_height
        elif normalize:
            # test_transform = train_transform = transforms.Compose([
            #     ResizePad(width, height),
            #     transforms.RandomCrop( (width, height), padding=None, pad_if_needed=True, fill=0, padding_mode='constant'),
            #     transforms.ToTensor(), 
            # ])
            # Imagenet resize
            test_transform = train_transform = transforms.Compose([
                transforms.Resize(resize_width),
                transforms.CenterCrop(crop_width),
                transforms.ToTensor(),
                Normalize(normalize_mean, normalize_std),
                # transforms.Normalize(
                #     mean=normalize_mean,
                #     std=normalize_std),
            ])
            width = crop_width
            height = crop_width
        else:
            # test_transform = train_transform = transforms.Compose([
            #     ResizePad(width, height),
            #     transforms.RandomCrop( (width, height), padding=None, pad_if_needed=True, fill=0, padding_mode='constant'),
            #     transforms.ToTensor(), 
            # ])
            # Imagenet resize
            test_transform = train_transform = transforms.Compose([
                transforms.ToTensor(),
            ])
            width = None
            height = None

        default_loaders = [{'set':'train', 'dataset': dest, 'enable_transform':True,  'transform':train_transform, 'sampler':'random', 'shuffle':True, 'mixup': True},
                           {'set':'val',   'dataset': dest, 'enable_transform':False, 'transform':test_transform,  'sampler':'sequential', 'shuffle':False, 'mixup': True}]

        loaders = default_loaders

    startIndex = 0
    allocated = 0.0
    remove_samples = [{'index':997, 'dir': 'n13054560'}] # Remove class 997 directory n13054560 matching pytorch pretraining: https://pytorch.org/vision/main/models/generated/torchvision.models.resnet101.html

    for i, loader in enumerate(loaders):

        imagenet_data = datasets.ImageNet(loader['dataset'], split=loader['set'], transform=loader['transform'])

        for remove_sample in remove_samples:
            dir_path = '{}{}/{}'.format(loader['dataset'],loader['set'], remove_sample['dir'])
            files = os.listdir(dir_path)
 
            for image_file in files:
                impath = os.path.join(dir_path, image_file)
                if os.path.isfile(impath):
                    imagenet_data.imgs.remove((impath,remove_sample['index']))

        if 'sampler' in loader and loader['sampler'] == 'ra_sampler':
            sampler = RASampler(imagenet_data, shuffle=loader['shuffle'], repetitions=ra_reps)
        elif 'sampler' in loader and loader['sampler'] == 'distributed':
            sampler = torch.utils.data.distributed.DistributedSampler(imagenet_data, shuffle=loader['shuffle'])
        else:
            if loader['shuffle']:
                sampler = torch.utils.data.RandomSampler(imagenet_data)
            else:
                sampler = torch.utils.data.SequentialSampler(imagenet_data)

        # Creating PT data samplers and loaders:
        loader['batches'] =int(imagenet_data.__len__()/batch_size)
        loader['length'] = loader['batches']*batch_size
        loader['width']=width
        loader['height']=height
        loader['in_channels']=3
        loader['num_classes']=len(ImagenetClasses)
        loader['classes']=ImagenetClasses

        collate_fn = None
        mixup_transforms = []
        if loader['mixup'] is True and mixup_alpha > 0.0:
            mixup_transforms.append(mixuptransforms.RandomMixup(loader['num_classes'], p=1.0, alpha=mixup_alpha))
        if loader['mixup'] is True and cutmix_alpha > 0.0:
            mixup_transforms.append(mixuptransforms.RandomCutmix(loader['num_classes'], p=1.0, alpha=cutmix_alpha))
        if mixup_transforms:
            mixupcutmix = transforms.RandomChoice(mixup_transforms)

            def collate_fn(batch):
                return mixupcutmix(*default_collate(batch))
        

        loader['dataloader'] = torch.utils.data.DataLoader(imagenet_data,
                                                batch_size=batch_size,
                                                #sampler=sampler,
                                                shuffle=False,
                                                num_workers=num_workers,
                                                pin_memory=pin_memory,
                                                collate_fn=collate_fn,)

    return loaders

def main(args):

    s3, creds, s3def = Connect(args.credentails)

    parameters = ReadDict(args.test_config)

    loaders = CreateImagenetLoaders(s3, s3def, 
                                args.obj_src, 
                                args.destination,
                                augment=parameters['imagenet']['augment'], 
                                normalize=parameters['imagenet']['normalize'], 
                                resize_width=parameters['imagenet']['resize_width'], 
                                resize_height=parameters['imagenet']['resize_height'],
                                crop_width=parameters['imagenet']['crop_width'], 
                                crop_height=parameters['imagenet']['crop_height'], 
                                batch_size=parameters['imagenet']['batch_size'], 
                                num_workers=parameters['imagenet']['num_workers'],
                                flipX=parameters['imagenet']['flipX'], 
                                flipY=parameters['imagenet']['flipY'], 
                                rotate=parameters['imagenet']['rotate'], 
                                scale_min=parameters['imagenet']['scale_min'], 
                                scale_max=parameters['imagenet']['scale_max'], 
                                offset=parameters['imagenet']['offset'], 
                                augment_noise=parameters['imagenet']['augment_noise'])

    parameters['imagenet']['test_path']=os.path.join(parameters['imagenet']['test_path'], '') # Add trailing slash if not present
    os.makedirs(parameters['imagenet']['test_path'], exist_ok=True)

    for loader in tqdm(loaders, desc="Loader"):
        for i, data in tqdm(enumerate(loader['dataloader']), 
                            desc="Batch Reads", 
                            total=loader['batches']):
            sample, target = data
            assert(sample is not None)
            assert(sample.shape[0] == parameters['imagenet']['batch_size'])
            if loader['height'] is not None:
                assert(sample.shape[2] == loader['height'])
            if loader['width'] is not None:
                assert(sample.shape[3] == loader['width'])
            assert(target is not None)

            if parameters['imagenet']['save_image']:
                sample =  sample.permute(0, 2, 3, 1) # Change to batch, height, width, channel for rendering
                sample_max = sample.max()
                sample_min = sample.min()
                if sample_max > sample_min:
                    for j, image in enumerate(sample):
                        image = 255*(image - sample_min)/(sample_max-sample_min) # Convert to RGB color rane
                        image = image.cpu().numpy().astype(np.uint8)
                        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                        write_path = '{}{}{:03d}{:03d}.png'.format(parameters['imagenet']['test_path'], loader['set'], i,j)            
                        cv2.imwrite(write_path,image)

            if parameters['imagenet']['test_images'] is not None and parameters['imagenet']['test_images'] > 0 and (i+1)*parameters['imagenet']['batch_size'] >= parameters['imagenet']['test_images']:
                print ('test_iterator complete')
                break

    print('Test complete')

#objdict = json.load(open('/data/git/mllib/datasets/coco.json'))
#Test(objdict, '/store/Datasets/coco/instances_val2017.json', '/store/Datasets/coco/val2014', 'COCO_val2014_')

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process arguments')

    parser.add_argument('-d', '--debug', action='store_true',help='Wait for debuggee attach')   
    parser.add_argument('-debug_port', type=int, default=3000, help='Debug port')
    parser.add_argument('-debug_address', type=str, default='0.0.0.0', help='Debug port')
    parser.add_argument('-credentails', type=str, default='creds.yaml', help='Credentials file.')
    parser.add_argument('-num_images', type=int, default=None, help='Number of images to display')
    parser.add_argument('-num_workers', type=int, default=25, help='Data loader workers')
    parser.add_argument('-batch_size', type=int, default=1, help='Dataset batch size')
    parser.add_argument('-i', action='store_true', help='True to test iterator')
    parser.add_argument('-test_iterator', type=bool, default=False, help='True to test iterator')
    parser.add_argument('-ds', action='store_true', help='True to test dataset')
    parser.add_argument('-test_dataset', action='store_true', help='True to test dataset')
    parser.add_argument('-test_path', type=str, default='./datasets_test/', help='Test path ending in a forward slash')
    parser.add_argument('-test_config', type=str, default='test.yaml', help='Test configuration file')

    parser.add_argument('-obj_src', type=str, default='data/imagenet', help='Object storage dataset source')
    #parser.add_argument('-destination', type=str, default='/data/datsets', help='Object storage dataset source')
    parser.add_argument('-destination', type=str, default='/nvmestore/mlstore/mllib/data/imagenet', help='Object storage dataset source')

    parser.add_argument('-height', type=int, default=224, help='Batch image height')
    parser.add_argument('-width', type=int, default=224, help='Batch image width')
    parser.add_argument('-imflags', type=int, default=cv2.IMREAD_COLOR, help='cv2.imdecode flags')
    parser.add_argument('-cuda', type=bool, default=True, help='pytorch CUDA flag') 
    parser.add_argument('-numTries', type=int, default=3, help="Read retries")

    args = parser.parse_args()

    if args.i:
        args.test_iterator = True

    if args.ds:
        args.test_dataset = True

    return args
    
if __name__ == '__main__':
    import argparse
    args = parse_arguments()

    if args.debug:
        print("Wait for debugger attach on {}:{}".format(args.debug_address, args.debug_port))
        import debugpy

        debugpy.listen(address=(args.debug_address, args.debug_port)) # Pause the program until a remote debugger is attached
        debugpy.wait_for_client()  # Pause the program until a remote debugger is attached
        print("Debugger attached")

    main(args)

