# CSS


## Styles

- `color`               : Can be text, rgb, rgba, hex or hsl format.
- `background-color`    : Can be text, rgb, rgba, hex or hsl format.
- `background`
  - `linear-gradient`           : Format -> `direction` `color...`
  - `repeating-linear-gradient` : Format -> `direction` `color length,...`
  - `url`                       : Format -> `link`

<br/>

- `font-size`           : Value in px or em.
- `font-family`         : Format for a backup font -> `initial font, backup font`
- `font-weight`         : Boldness of the font.

<br/>

- `width`               : Value in px or %.
- `height`              : Value in px or %.
- `max-width`
- `max-height`

<br/>

- `border`              : Format -> `border-width` `border-style` `border-color`
- `border-color`        : Can be text, rgb, rgba, hex and hsl.
- `border-width`        
- `border-style`        : Can be dotted, dashed, double or solid.
  - Format 1: top right bottom left
  - Format 2: top [right & left] bottom
  - Format 3: [top & bottom] [right & left]
  - Format 4: All
- `border-radius`       : Value in px or %. (50% is a circle)

<br/>

- `box shadow`          : Format -> `offset-x` `offset-y` `blur-radius` `spread-radius` `color`
- `opacity`

<br/>

- `padding`             : Spacing between border and content
- `padding-[n]`         : n can be top/bottom/right/left

<br/>

- `margin`              : Spacing between border and outside elements.
- `margin-[n]`          : n can be top/bottom/right/left

<br/>

- `text-align`          : Can be set to justify, left, right or center
- `text-transform`      : Can be lowercase, uppercase, capitalize, initial, inherit or none.
- `line-height`         : Value in px.
- `transform`
  - `scale`
  - `skewX`
  - `skewY`

<br/>

- `float`               : Almost like fixed but for left or right.
- `z-index`             : Can be used to order the layout of the elements.
- `position`            : Can be relative, absolute, fixed or sticky.
  - `top`
  - `bottom`
  - `left`
  - `right`

<br/>

- `animation-name`      : Sets name of animation
- `animation-duration`
- `animation-fill-mode`
- `animation-iteration-count` : Can be a number or infinite.
- `animation-timing-function` : Can be ease(default), ease-in, ease-out or linear.
  - cubic-beizer function can also be used as a timing function.

<br/>

- `display`             : Can be flex or grid

<br/>

- `flex-direction`      : Can be row, column, row-reverse or oclumn-reverse
- `justify-content`     : Horizontal Alignment. Can be flex-start, flex-end, space-between, space-around or space-evenly.
- `align-items`         : Vertical Alignment. Can be flex-start, flex-end, center, stretch and baseline.
- `flex-wrap`           : Can be wrap, wrap-reverse or none.
- `flex-shrink`
- `flex-grow`
- `flex-basis`
- `flex`                : `flex-grow` `flex-shrink` `flex-basis`
- `order`
- `align-self`          : Overrides `align-items`

<br/>

- `grid-template-[rows | columns]`  : Defines the number and size of each row or column.
  - `repeat`
  - `autofill`
  - `minmax`
- `grid-[row | column]-gap`         : Spacing between adjacent rows or columns
- `grid-gap`                        : Shorthand for `grid-[row | column]-gap` or a common value for both.
- `grid-[column | row]`             : Amount of space that a item takes.
- `justify-[self | items]`          : Vertical Alignment for single item / all items. Can be start, center or end.
- `align-[self | items]`            : Horizontal Alignment for single item / all items. Can be start, center or end.
- `grid-template-areas`             : For container
- `grid-areas`                      : For item


## Class Types

- Class         :   Starts with a period(`.`)
- HTML elements :   Named the same way as the tag is.
- Id            :   Starts with a hash(`#`)
- Type          :   Format is `[attr = value]`
- Psuedo Class  :   Format is `[element]:{pseudo-class}`

<br/>

## CSS Selectors
- Descendant        : Selects all descendants of the first that are the second. Example: `div a{}`
- Adjacent Sliding  : Siblings in order. Example: `div+a{}`
- Child             : Immidiate children. Examples: `div > a{}`
- General Sibling   : Next siblings. Examples: `div ~ a{}`

<br/>

## Override Order (Most to least)

1.  !important
2.  Inline Style Tag
3.  Id
4.  Class, Pseudo-Class, Attribute
5.  Element


<br/>
Last definition counts when multiple of the same level are declared.

<br/>

## Variables

- Variables start with a (`--`). Example: `--background-color`. 
- Values can be invoked by using var([var-name]). Example: `var(--background-color)`
- Fallback values can be used inside the var parentheses. Example `var(--background-color, red)`
- Inhertitance takes place just like classes work.
- Reassigning variables is also possible.

<br/>

## Media Query

- Media queries can be used to change classes and reassign variables.
- It can also be used to set extra attributes or change them.
- Arguments:
  - `min-height`
  - `min-width`
  - `max-height`
  - `max-width`

<br/>

## Keyframe
Each keyframe block is followed by the animation name.

Each percentage configuration block includes the configuration based on time.


<br/>

## Miscellaneous

- Retina Images have have the width and height of the original resolution.
- Viewport units correspond to device size.
  - vh
  - vw
  - vmin
  - vmax
- [Link for pseudo classes](https://www.w3schools.com/css/css_pseudo_classes.asp)
- 
