import json, math

def tenths(x):
    return math.floor(x * 10 + 0.5) / 10

def fixed1(x):
    return f"{tenths(x):.1f}"

def article(n):
    s = str(abs(int(n)))
    return "An" if s.startswith("8") or s.startswith("11") or s.startswith("18") else "A"

def custard_truth(eggs, dairy):
    if eggs <= 0:
        raise ValueError("the egg count must be above zero")
    if dairy <= 0:
        raise ValueError("the dairy must be above zero")
    per = tenths(dairy / eggs)
    if per < 0.4:
        band = "firmer and richer than the classic ratio"
    elif per <= 0.6:
        band = "right at the classic ratio"
    else:
        band = "looser than the classic ratio, so the wobble risks weeping"
    return (f"{article(eggs)} {eggs}-egg batch with {fixed1(dairy)} cups of dairy "
            f"pours {fixed1(per)} cups per egg, {band} honestly.")

def batch_truth(eggs, dairy):
    if eggs <= 0:
        raise ValueError("the egg count must be above zero")
    if dairy <= 0:
        raise ValueError("the dairy must be above zero")
    total = tenths(dairy + eggs * 0.2)
    return (f"{article(eggs)} {eggs}-egg batch with {fixed1(dairy)} cups of dairy "
            f"makes {fixed1(total)} cups of custard honestly.")

def pan_truth(total, pan):
    if total <= 0:
        raise ValueError("the custard must be above zero")
    if pan <= 0:
        raise ValueError("the pan size must be above zero")
    cap = tenths(4 * (pan / 9) ** 2)
    diff = tenths(cap - total)
    if diff > 0:
        verdict = f"fits with {fixed1(diff)} cups to spare"
    elif diff == 0:
        verdict = "fills it to the brim exactly"
    else:
        verdict = f"overflows by {fixed1(-diff)} cups"
    return (f"{fixed1(total)} cups of custard in {article(pan).lower()} {pan}-inch dish "
            f"rated about {fixed1(cap)} cups {verdict} honestly.")

cases = []

def add(fn_name, args):
    try:
        fn = {"custardTruth": custard_truth, "batchTruth": batch_truth, "panTruth": pan_truth}[fn_name]
        result = fn(*args)
        cases.append({"fn": fn_name, "args": args, "result": result})
    except ValueError as e:
        cases.append({"fn": fn_name, "args": args, "error": str(e)})

# custardTruth
add("custardTruth", [4, 2])      # classic 0.5
add("custardTruth", [8, 4])      # An 8-egg article, classic
add("custardTruth", [1, 0.5])    # singular egg, classic
add("custardTruth", [4, 1.2])    # 0.3 firmer
add("custardTruth", [4, 2.8])    # 0.7 looser
add("custardTruth", [6, 3])      # 0.5 classic
add("custardTruth", [5, 2])      # 0.4 edge -> classic
add("custardTruth", [5, 3.5])    # 0.7 looser
add("custardTruth", [3, 1.2])    # 0.4 edge -> classic
add("custardTruth", [3, 1.1])    # 0.366 -> 0.4 rounded -> classic (judges rounded)
add("custardTruth", [0, 2])      # error
add("custardTruth", [4, 0])      # error
# batchTruth
add("batchTruth", [4, 2])        # 2.8
add("batchTruth", [8, 4])        # 5.6, An 8-egg
add("batchTruth", [1, 0.5])      # 0.7 singular
add("batchTruth", [3, 1.5])      # 2.1
add("batchTruth", [6, 3])        # 4.2
add("batchTruth", [0, 2])        # error
add("batchTruth", [4, 0])        # error
# panTruth
add("panTruth", [2.8, 9])        # cap 4.0, 1.2 spare
add("panTruth", [4.0, 9])        # exactly
add("panTruth", [5.0, 9])        # overflows 1.0
add("panTruth", [2.0, 8])        # an 8-inch, cap 3.2, 1.2 spare
add("panTruth", [3.2, 8])        # exactly at 8-inch
add("panTruth", [2.8, 11])       # an 11-inch, cap 6.0, 3.2 spare
add("panTruth", [1.0, 10])       # a 10-inch, cap 4.9, 3.9 spare
add("panTruth", [0, 9])          # error
add("panTruth", [2.8, 0])        # error

with open("expected.json", "w") as f:
    json.dump(cases, f, indent=2)
print(f"{len(cases)} cases written")
for c in cases:
    print(c["fn"], c["args"], "->", c["result"] if "result" in c else "ERR: " + c["error"])
