// Quiche Math engine - custard ratio, batch volume and pan fit honesty.
// Every norm is a labeled kitchen norm; the app never judges doneness or safety.

function assertPositive(value, label) {
  if (!Number.isFinite(value) || value <= 0) {
    throw new Error(label + " must be above zero");
  }
}

function tenths(x) {
  return Math.floor(x * 10 + 0.5) / 10;
}

function fixed1(x) {
  return tenths(x).toFixed(1);
}

function article(n) {
  const s = String(Math.abs(Math.trunc(n)));
  return (/^([8]|11|18)/.test(s)) ? "An" : "A";
}


// Labeled norm: the classic quiche custard is 1 egg to half a cup of dairy.
function custardTruth(eggs, dairyCups) {
  assertPositive(eggs, "the egg count");
  assertPositive(dairyCups, "the dairy");
  const per = tenths(dairyCups / eggs);
  let band;
  if (per < 0.4) {
    band = "firmer and richer than the classic ratio";
  } else if (per <= 0.6) {
    band = "right at the classic ratio";
  } else {
    band = "looser than the classic ratio, so the wobble risks weeping";
  }
  return article(eggs) + " " + eggs + "-egg batch with " + fixed1(dairyCups) +
    " cups of dairy pours " + fixed1(per) + " cups per egg, " + band + " honestly.";
}

// Labeled norm: a large egg is about a fifth of a cup.
function batchTruth(eggs, dairyCups) {
  assertPositive(eggs, "the egg count");
  assertPositive(dairyCups, "the dairy");
  const total = tenths(dairyCups + eggs * 0.2);
  return article(eggs) + " " + eggs + "-egg batch with " + fixed1(dairyCups) +
    " cups of dairy makes " + fixed1(total) + " cups of custard honestly.";
}

// Labeled norm: a 9-inch pie dish holds about 4 cups at the same depth, and capacity scales with pan area.
function panTruth(totalCups, panInches) {
  assertPositive(totalCups, "the custard");
  assertPositive(panInches, "the pan size");
  const cap = tenths(4 * Math.pow(panInches / 9, 2));
  const diff = tenths(cap - totalCups);
  let verdict;
  if (diff > 0) {
    verdict = "fits with " + fixed1(diff) + " cups to spare";
  } else if (diff === 0) {
    verdict = "fills it to the brim exactly";
  } else {
    verdict = "overflows by " + fixed1(-diff) + " cups";
  }
  return fixed1(totalCups) + " cups of custard in " + article(panInches).toLowerCase() + " " + panInches +
    "-inch dish rated about " + fixed1(cap) + " cups " + verdict + " honestly.";
}

if (typeof module !== "undefined") {
  module.exports = { custardTruth, batchTruth, panTruth, tenths, fixed1 };
}
