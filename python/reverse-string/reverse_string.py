def reverse(text):
  if text == "":
    return ""
  new_str = list(text)
  left = 0
  right = len(new_str)-1
  while left < right:
    new_str[left], new_str[right] = new_str[right], new_str[left]
    left += 1
    right -= 1
  result = ""
  for x in new_str:
    result += x
  return result
