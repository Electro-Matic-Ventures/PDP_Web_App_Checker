split_pn = {
    "pdp": "B1",
    "type": "C1",
    "certificate": "D1",
    "language": "E1",
    "voltage": "F1",
    "main_breaker": "G1",
    "small_breakers": "H1",
    "large_breakers": "J1",
    "isolation_transformer": "L1",
    "phase_transformer": "N1",
    "feed": "P1"
}

output = ''
for key in split_pn:
    output += f'Call address.set_features("{key}", "{split_pn[key]}")\n'
with open('output.txt', 'w') as file_:
    file_.write(output)
