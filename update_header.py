import os

files_to_update = [
    'index.html',
    'privacy-policy.html',
    'terms-of-stay.html',
    'cancellation-and-refund.html'
]

logo_tag = '<img alt="Karnataka Pravasi Soudha Tirumala Logo" class="h-8 w-auto object-contain" src="./logo.svg"/>'
old_title_html = '<a class="font-headline-sm text-headline-sm text-primary tracking-tight leading-none hover:text-primary-container transition-colors" data-path="home" href="#">Karnataka Pravasi Soudha</a><span class="font-label-sm text-label-sm text-secondary tracking-wider uppercase mt-0.5">Tirumala Kshetra · Pilgrim Guest House</span>'

new_title_html = '<a class="font-headline-sm text-[18px] sm:text-headline-sm text-primary tracking-tight leading-none hover:text-primary-container transition-colors truncate" data-path="home" href="#">Karnataka Pravasi Soudha</a><span class="font-label-sm text-[10px] sm:text-label-sm text-secondary tracking-wider uppercase mt-0.5 truncate">Tirumala Kshetra <span class="hidden sm:inline">· Pilgrim Guest House</span></span>'

# Also let's fix the layout of the header left side so it doesn't overflow
# <div class="flex flex-col"> to <div class="flex flex-col overflow-hidden max-w-[200px] sm:max-w-none">
old_div = '<div class="flex flex-col">' + old_title_html
new_div = '<div class="flex flex-col overflow-hidden max-w-[220px] sm:max-w-none">' + new_title_html

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            content = f.read()
        
        # Remove logo
        content = content.replace(logo_tag, '')
        
        # Replace title HTML
        content = content.replace(old_div, new_div)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Updated {filename}")
