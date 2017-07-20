---
config_dir: /home/travis/.jupyter
kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  codemirror_mode:
    name: ipython
    version: 3
  file_extension: .py
  mimetype: text/x-python
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
  version: 3.5.3
layout: post
metadata:
  modified_date: July 20, 2017
  name: 2017-07-06-The-Alphabet-Cipher
  path: whatever
output_extension: .md
output_files_dir: 2017-07-06-The-Alphabet-Cipher_files
title: Encrypting and Decrypting 'The Alphabet Cipher`
unique_key: 2017-07-06-The-Alphabet-Cipher

---

# The alphabet cipher challenge

Created for the [pyatl jam session](https://www.meetup.com/python-atlanta/events/237560615/)

Cyber dojo 👉 40A6A54C18

---

* https://en.wikipedia.org/wiki/The_Alphabet_Cipher

This literate code document is written Markdown first; all code elements are executed as Python.

        !pip install git+https://github.com/tonyfast/literacy



<div class="output_markdown rendered_html output_subarea ">
<p>Create the alphabet using <code>range, ord and chr</code>.</p>

<pre><code>alphabet = ''.join(map(chr, range(ord('a'), ord('z')+1)))    </code></pre>

</div>


<div class="output_markdown rendered_html output_subarea ">
<p>Construct the alphabet cipher and call it <strong>tabula</strong>; this table is the mapping for the encryption.</p>

<pre><code>__tabula__ = [''.join([

</code></pre>
<p>Shift the alphabet by the current <strong>row</strong></p>

<pre><code>    *alphabet[i:], *alphabet[:i]

</code></pre>
<p>The current row maps directly to the letter in an alphabet.</p>

<pre><code>]) for i in range(26)]</code></pre>

</div>


<div class="output_markdown rendered_html output_subarea ">
<p><strong><code>Ł = alphabet.index</code></strong> converts a letter to an index.</p>

</div>


<div class="output_markdown rendered_html output_subarea ">
<h2 id="Solving-the-problem">Solving the problem<a class="anchor-link" href="#Solving-the-problem">&#182;</a></h2><p>Use <code>key = 'vigilance'</code> to <strong>encrypt</strong> <code>message = 'meetmeontuesdayeveningatseven'</code> with the 
<strong>tabula</strong> constructed above.</p>

</div>


<div class="output_markdown rendered_html output_subarea ">
<p>This cipher requires that the key and message are the same length; <strong>regularize</strong> performs this task</p>

<pre><code>def regularize(key, message):
    while len(key) &lt; len(message):
        key += key
    return zip(key[:len(message)], message)</code></pre>

</div>


<div class="output_markdown rendered_html output_subarea ">

<pre><code>def encrypt(key, message):
    return ''.join([


</code></pre>
<p>Look-up the <code>message</code> character's row for it's corresponding <code>key</code>; 
the value os the encrypted character</p>

<pre><code>        __tabula__[Ł(_)][Ł(__)] for _, __ in regularize(key, message)])</code></pre>

</div>


<div class="output_markdown rendered_html output_subarea ">
<p><code>secret = encrypt(key, message)</code>, the <code>secret</code> <strong>encrypt</strong>ed <code>message</code> is <code>secret</code>.</p>

</div>




    'hmkbxebpxpmyllyrxiiqtoltfgzzv'




<div class="output_markdown rendered_html output_subarea ">
<h2 id="Inverse-encryption-or-decryption">Inverse encryption or <strong>decrypt</strong>ion<a class="anchor-link" href="#Inverse-encryption-or-decryption">&#182;</a></h2>
<pre><code>def decrypt(key, secret):

    return ''.join([
        chr([

</code></pre>
<p><strong>pluck</strong> the <strong>key</strong> letters from each row</p>

<pre><code>            row[Ł(_)] for row in __tabula__

</code></pre>
<p>and find the index of the <strong>secret</strong></p>

<pre><code>        ].index(__) + ord('a')) 

</code></pre>
<p>over each of the letters in the (key, secret) pairs</p>

<pre><code>        for _, __ in regularize(key, secret)])</code></pre>

</div>


<div class="output_markdown rendered_html output_subarea ">

<pre><code>decrypt(key, secret)</code></pre>

</div>




    'meetmeontuesdayeveningatseven'




<div class="output_markdown rendered_html output_subarea ">
<p>The secret puzzle is <code>decrypt('PYATLJAMSESSION'.lower(), 'LFAMTBTTWEAJADRTBVXWXCULCGXIBHCJAWPWSISPDGE'.lower())</code></p>

</div>




    'whatistheairspeedvelocityofanunladenswallow'


---

# Example lookup


    v i g i l a n c e v i g i l a n c e v i g i l a n c e v i
    m e e t m e o n t u e s d a y e v e n i n g a t s e v e n
    h m k b x e b p x p m y l l y r x i i q t o l t f g z z v
