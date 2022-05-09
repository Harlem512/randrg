import PySimpleGUI as sg
import random as rng
# rng.randint(0, 10) inc 0,10

# DRG Build Randomizer by Harlem512
# Updated for Season 2

classes = ['Driller', 'Engineer', 'Gunner', 'Scout']
primary = [['Flame', 'Cryo', 'Sludge'],
    ['Warthog', 'Stubby', 'LOKI'],
    ['Minigun', 'Auto', 'Hurricane'],
    ['Deepcore', 'M1000', 'DRAK']]
primaryUpgrades = [[23332, 33232, 33223],
    [23322, 33222, 23323],
    [32333, 33323, 32223],
    [22333, 23223, 32332]]
primaryOC = [[
        ['Lighter Tanks', 'Sticky Additive', 'Compact Feed Valves', 'Fuel Stream Diffuser', 'Face Melter', 'Sticky Fuel'],
        ['Improved Thermal Efficiency', 'Tuned Cooler', 'Flow Rate Expansion', 'Ice Spear', 'Ice Storm', 'Snowball'],
        ['Hydrogen Ion Additive', 'AG Mixture', 'Volatile Impact Mixture', 'Disperser Compound', 'Goo Bomber Special', 'Sludge Blast']
    ],[
        ['Stunner', 'Light-Weight Magazines', 'Magnetic Pellet Alignment', 'Cycle Overload', 'Minishells'],
        ['Super-Slim Rounds', 'Well Oiled Machine', 'EM Refire Booster', 'Light-Weight Rounds', 'Turret Arc', 'Turret EM Discharge'],
        ['Armor Break Module', 'Eraser', 'Seeker Rounds', 'Explosive Chemical Rounds', 'Executioner', 'Neuro-Lasso']
    ], [
       ['A Little More Oomph!', 'Thinned Drum Walls', 'Burning Hell', 'Compact Feed Mechanism', 'Exhaust Vectoring', 'Bullet Hell', 'Lead Storm'],
       ['Composite Drums', 'Splintering Shells', 'Carpet Bomber', 'Combat Mobility', 'Big Bertha', 'Neurotoxin Payload'],
       ['Manual Guidance Cutoff', 'Overtuned Feed Mechanism', 'Fragmentation Missiles', 'Plasma Burster Missiles', 'Minelayer System', 'Jet Fuel Homebrew', 'Salvo Module'] 
    ], [
        ['Compact Ammo', 'Gas Rerouting', 'Homebrew Powder', 'Overclocked Firing Mechanism', 'Bullets of Mercy', 'AI Stability Engine', 'Electrifying Reload'],
        ['Hoverclock', 'Minimal Clips', 'Active Stability System', 'Hipster', 'Electrocuting Focus Shots', 'Supercooling Chamber'],
        ['Impact Deflection', 'Thermal Liquid Coolant', 'Rewiring Mod', 'Aggressive Venting', 'Overtuned Particle Accelerator', 'Shield Battery Booster', 'Thermal Exhaust Feedback']
    ]]
secondary = [['Subata', 'EPC', 'Cooker'],
    ['Deepcore', 'Breach', 'Shard'],
    ['Bulldog', 'BRT', 'Coilgun'],
    ['Boomstick', 'Zhukov', 'Boltshark']]
secondaryUpgrades = [[32322, 32333, 33223],
    [32333, 23223, 32223],
    [23322, 33232, 33223],
    [22333, 23232, 33223]]
secondaryOC = [[
        ['Chain Hit', 'Homebrew Powder', 'Oversized Magazine', 'Automatic Fire', 'Explosive Reload', 'Tranquilizer Rounds'],
        ['Energy Rerouting', 'Magnetic Cooling Unit', 'Heat Pipe', 'Heavy Hitter', 'Overcharger', 'Persistent Plasma'],
        ['Liquid Cooling System', 'Super Focus Lens', 'Diffusion Ray', 'Mega Power Supply', 'Blistering Necrosis', 'Gamma Contamination']
    ],[
        ['Clean Sweep', 'Pack Rat', 'Compact Rounds', 'RJ250 Compound', 'Fat Boy', 'Hyper Propellant'],
        ['Light-Weight Cases', 'Roll Control', 'Stronger Plasma Current', 'Return to Sender', 'High Voltage Crossover', 'Spinning Death', 'Inferno'],
        ['Efficiency Tweaks', 'Automated Beam Controller', 'Feedback Loop', 'Volatile Impact Reactor', 'Endothermic Explosion', 'Overdrive Booster']
    ],[
        ['Chain Hit', 'Homebrew Powder', 'Volatile Bullets', 'Six Shooter', 'Elephant Rounds', 'Magic Bullets'],
        ['Composite Casings', 'Full Chamber Seal', 'Compact Mags', 'Experimental Rounds', 'Electro Minelets', 'Micro Flechettes', 'Lead Spray'],
        ['Ultra-Magnetic Coils', 'Backfeeding Module', 'Re-Atomizer', 'The Mole', 'Hellfire', 'Triple-Tech Chambers']
    ], [
        ['Compact Shells', 'Double Barrel', 'Special Powder', 'Stuffed Shells', 'Shaped Shells', 'Jumbo Shells'],
        ['Minimal Magazines', 'Custom Casings', 'Cryo Minelets', 'Embedded Detonators', 'Gas Recycling'],
        ['Quick Fire', 'The Specialist', 'Cryo Bolt', 'Fire Bolt', 'Bodkin Points', 'Trifork Volley']
    ]
]

grenade = [['Impact Axe', 'High Explosive', 'Neurotoxin'],
    ['LURE', 'Plasma Burster', 'Proximity Mine'],
    ['Sticky', 'Incendiary', 'Cluster'],
    ['Inhibitor-Field', 'Cryo', 'Pheromone']
]

mobilityNames = ['Drills', 'Platform', 'Zipline', 'Grapple']
utilityNames = ['C4', 'Turret', 'Shield', 'Flare']

mobilityUpgrades = [3212, 313, 312, 2123]
utilityUpgrades = [3123, 2332, 223, 223]
armor = 3213
pick = 13

active = ['Beast Master', 'Berzerker', 'Dash', 'Field Medic', 'Heightened Senses', 'Hover Boots', 'Iron Will', 'See You In Hell', 'Shield Link']
passive = ['Born Ready', 'Deep Pockets', 'Elemental Insulation', 'Friendly', 'It\'s a Bug Thing', 'Resupplier', 'Second Wind', 'Strong Arm', 'Sweet Tooth', 'Thorns', 'Unstoppable', 'Vampire', 'Veteran Depositor']

sg.theme('DarkAmber')   # Add a touch of color
sg.set_options(element_padding=(0,0))  

# All the stuff inside your window.
layout = [  [sg.Text('DRG Randomizer', size=(40,1))],
            [sg.Button('Randomize', key='unlucky'), sg.Button("I'm feeling lucky", key='lucky')],
            [sg.Text('Class'), sg.Text(key='class')],
            [sg.Text('Primary'), sg.Text(key='pr', size=(10,1)), sg.Text(key='prBld', size=(5,1)), sg.Text(key='prOc', size=(25,1))],
            [sg.Text('Secondary'), sg.Text(key='sc', size=(10,1)), sg.Text(key='scBld', size=(5,1)), sg.Text(key='scOc', size=(25,1))],
            [sg.Text('Mobility Tool'), sg.Text(key='mbName', size=(10,1)), sg.Text(key='mb')],
            [sg.Text('Utility Tool'), sg.Text(key='utName', size=(10,1)), sg.Text(key='ut')],
            [sg.Text('Grenade'), sg.Text(key='gn', size=(25,1))],
            [sg.Text('Armor'), sg.Text(key='ar')],
            [sg.Text('Pickaxe'), sg.Text(key='pk')],
            [sg.Text('Actives'), sg.Text(key='pa', size=(40,1))],
            [sg.Text('Passives'), sg.Text(key='pp', size=(40,1))]
        ]

# Create the Window
window = sg.Window('DRG Build Randomizer', layout, default_element_size=(10,1), auto_size_text=False, auto_size_buttons=False, default_button_element_size=(22,1), finalize=True)

# Ok this one's pretty bad
# Randomizes the upgrade numbers from the maximum for each option
def getNum(max: int):
    nums = 0
    for digit in str(max):
        nums *= 10
        nums += rng.randint(1, int(digit))
    return nums


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    if event == 'lucky' or event == 'unlucky':
        rClass = rng.randint(0,3)

        # The luck factor (25% more engineer)
        if event == 'lucky' and rng.randint(0,3) == 0:
            rClass = 1

        # Select primary/secondary
        rPrimary = rng.randint(0,2)
        rSecondary = rng.randint(0,2)

        window['class'].Update(classes[rClass])

        window['pr'].Update(primary[rClass][rPrimary])
        window['prBld'].Update(getNum(primaryUpgrades[rClass][rPrimary]))
        window['prOc'].Update(rng.choice(primaryOC[rClass][rPrimary]))

        window['sc'].Update(secondary[rClass][rSecondary])
        window['scBld'].Update(getNum(secondaryUpgrades[rClass][rSecondary]))
        window['scOc'].Update(rng.choice(secondaryOC[rClass][rSecondary]))

        window['mbName'].Update(mobilityNames[rClass])
        window['mb'].Update(getNum(mobilityUpgrades[rClass]))
        window['utName'].Update(utilityNames[rClass])
        window['ut'].Update(getNum(utilityUpgrades[rClass]))
        window['ar'].Update(getNum(armor))
        window['pk'].Update(getNum(pick))
        window['gn'].Update(grenade[rClass][rng.randint(0,2)])

        # Gets 2 random numbers from 0-X then converts to perk name, then makes them a pretty string
        window['pa'].Update(', '.join([active[p] for p in rng.sample(range(0,len(active)-1), 2)]))
        window['pp'].Update(', '.join([passive[p] for p in rng.sample(range(0,len(passive)-1), 3)]))

window.close()