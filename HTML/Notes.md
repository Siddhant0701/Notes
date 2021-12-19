# HTML

Notes about HTML.

<br/>

## Tags

- `<!doctype html>`     - needs to be used in html files.
- `<html>`              - Used as the root container.
- `<title>`             - Title for the website in the browser tabs.  
- `<head>`              - Includes metadata and other information about the website.
- `<body>`              - Includes the contents of the website.

<br/>

- `<p>`                 - Used to create paragraphs.
- `<h[n]>`              - Header tag. n represents the level of heading where 1 is the highest and 6 is the lowest.

<br/>

- `<img>`               - Used to add images. Attributes: `src`, `alt`.
- `<a>`                 - Used to add hyperlinks. Attributes: `href`.
  - External Links can be added directly.
  - Internal files can be added using dot notation.
  - Internal content can be added using the `id` attribute.
  - Dead links can be set using `#` as the image `src` or link `href`.

<br/>

- `<ul>`                - Creates an unordered list (bulleted list).
- `<ol>`                - Creates an ordered list. Attributes: `type = I/A/a/1/i`
- `<li>`                - Individal list items for ordered and unordered lists.
- `<dl>`                - Creates a description list.
- `<dt>`                - Description title for each list item.
- `<dd>`                - Text description for each item.
 
<br/>

- `<form>`              - Creates a form whose responses can be submitted using the `action` attribute.
- `<input>`             - Create an input field. Attributes: `type`, `required`.
- `<label>`             - Creates a label(text) for any input type such that the text can be used to access the input. Attributes: `for = [input id]`
  - `text`      - Creates a text field. Can be used with `placeholder` attribute.
  - `submit`    - Creates a submit button to submit responses of the form.
  - `radio`     - Creates a radio button. Single choice options. 
  - `checkbox`  - Creates a checkbox. Multiple choice options.
    - `name` attribute can be used to define groups of radio buttons or checkboxes. 
    - `value` attribute is the one that is sent to the form. 
    - `checked` attribute can be used to check buttons by default.

<br/>

- `<div>`               - Division of content. Used to apply classes. Block line element.
- `<span>`              - Division of content. Inline elements.

<br/>

- `<style>`             - Used for CSS styling inside the html file.
- `<link>`              - Used to import stylesheet information. Attributes: `rel`, `type`, `href`

<br/>

- `<b>`/`<strong>`      - Used to make the text bold.
- `<u>`                 - Used to make the text underlined.
- `<i>`/`<em>`          - Used to make the text italicized.
- `<s>`                 - Used to strikethrough the text.

<br/>

- `<hr>`                - Horizontal line division
- `<br>`                - Break line

<br/>

- `<main>`
- `<header>`
- `<footer>`
- `<nav>`
- `<article>`
- `<section>`
- `<figure>`
- `<figcaption>`
- `<time>`              - Attribute: `datetime`

<br/>

- `<fieldset>`          - Used to wrap around radio buttons or checkboxes
- `<legend>`            - Adding information for radio button groups or checkboxes.

<br/>

## Accessibility Attributes

- `accesskey`           - Can be used to access specific content with the right command (Windows: Alt+{key})
- `tabindex`            - Can be used to access content by pressing tab.

<br/>

## Comments

Comments start with `<!--` and end with `-->`. These can be single line or multiline.



