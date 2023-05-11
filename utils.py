def string_to_int(value):
  return int(value.replace(',',''))

def fit_value(upper_bound, value, max):
  return value * upper_bound/max