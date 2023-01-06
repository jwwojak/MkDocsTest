# Test protocol file from the opentrons website: https://docs.opentrons.com/v2/tutorial.html#tutorial
import asyncio


from opentrons import protocol_api

metadata = {
    'apiLevel': '2.13',
    'protocolName': 'Serial dilution tutorial',
    'description': '''This protocol is from the Opentrons Python tutorial.
                    It takes a solution and progressively dilutes it by transferring it stepwise
                    across all the wells in a plate.''',
    'author': 'Joe'
}

def run(protocol: protocol_api.ProtocolContext):
    tips = protocol.load_labware('opentrons_96_tiprack_300ul', 1) #load pipette tip rack
    reservoir = protocol.load_labware('nest_12_reservoir_15ml', 2) # load reservoir
    plate = protocol.load_labware('nest_96_wellplate_200ul_flat', 3) # load well plate
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tips]) #load pipettes, specify last b/c tips need to go first
    
    p300.transfer(100, reservoir['A1'], plate.wells())
    
    for i in range(8):
        row = plate.rows()[i]
        p300.transfer(100, reservoir['A2'], row[0], mix_after=(3, 50))
        p300.transfer(100, row[:11], row[1:], mix_after=(3, 50))
