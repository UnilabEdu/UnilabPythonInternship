# css

[![intro to CSS](https://res.cloudinary.com/marcomontalbano/image/upload/v1616768772/video_to_markdown/images/google-drive--1iJQL4D6oVdF443WuhzFwl--4H1__1bvK-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1iJQL4D6oVdF443WuhzFwl--4H1__1bvK/view?usp=sharing "intro to CSS")

**cascading style sheets** ( CSS ) აღწერს თუ როგორ გამოჩნდება HTML ელემენტები ვებ გვერდზე.
CSS შეუძლია რამოდენიმე სხვადასხვა გვერდზე განლაგებულ ელემენტებზე იქონიოს გავლენა. სტილის დაწერა შეგვიძლია თვითონ html დოკუმენტში, კონკრეტულ html ელემენტზე და დაკავშირებულ ფაილში, მაგ.: `style.css`

## ტერმინოლოგია და ანატომია
![ანატომია](https://mdn.mozillademos.org/files/9461/css-declaration-small.png)

დასახელება | გამოყენება
--- | ---
Selector | ტეგის სელექტორი
Property | პარამეტრი
Property Value | მნიშვნელობა
Declaration | გაწერა (სტილის)

### მაგალითი: 
```css
p {
  background-color: lightblue;
  color: white;
  text-align: center;
  font-family: serif;
  font-size: 20px;
}
```

## სტილის უპირატესობის იერარქია

- inline style - გულისხმობს კონკრეტულ html ელემენტზე გაწერილ სტილს. ამისთვის გამოიყენება style ატრიბუტი. ამგვარი სტილი უპირატესია ყველა სხვა ფორმით გაწერილ სტილზე.

```html
<p style="color: red">This is a paragraph.</p>
```

- internal style - გულისხმობს html დოკუმენტში გაწერილ სტილს. ამისთვის `<head> </head>` ბლოკში გამოიყენება `<style> </style>`. ამგვარი სტილი არაა უპირატესი inline სტილზე.

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>

    <style>
      h1 {
        color: blue;
      }
    </style>
  </head>

  <body>
    <h1>This is a heading</h1>
  </body>
</html>
```

- external style - გულისხმობს დამოუკიდებელ css დოკუმენტში გაწერილ სტილს. ამისთვის html დოკუმენტს `<head> </head>` ბლოკში უნდა დავუკავშიროთ css დოკუმენტი. ამგვარი სტილი არაა უპირატესი inline სტილზე.

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="./style.css" />
    <title>Document</title>
  </head>

  <body>
    <h1>This is a heading</h1>
  </body>
</html>
```

ატრიბუტი `rel` აღნიშნავს ბმული ფაილის ტიპს/როლს _html_ ფაილისთვის, ხოლო
`href`-ში თავსდება იმ ფაილის მისამართი სადაც სტაილშიტია მოთავსებული.

## class და id

ყოველ HTML ელემენტს აქვს შესაძლებლობა მიენიჭოს class ან id ატრიბუტი. ამ ატრიბუტების დახმარებით შეგვიძლია მივწვდეთ სასურველ ელემენტებს.

**class**-ის გამოყენებით შეგვიძლია გავაერთიანოთ სხვადასხვა (თუნდაც არაერთგვაროვანი ტიპის) html
ელემენტი და მივანიჭოთ მათ საერთო მახასიათებელი.

**id**-ის მეშვეობით შეგვიძლია ინდივიდუალურად ავირჩიოთ html ელემენტი რომელზეც გვსურს რეაგირება.
შესაბამისად ყოველ ელემენტს უნდა ჰქონდეს უნიკალური ინდივიდუალური id მნიშვნელობა.

## css სინტაქსი:

`#` - გამოიყენება id-ის გამოსაძახებლად
`.` - გამოიყენება class-ის გამოსაძახებლად

მაგალითად:

```css
.class {
  background: maroon;
}

#id {
  background: green;
}
```
## სხვა ხშირად გამოყენებადი პარამეტრები
### ფონი
**ფონური ფერი**ს არჩევა:
```css
{
    background: gray;
}
```
ან ფერის არჩევა [ჰექს კოდით](https://www.color-hex.com/)
```css
{
    background: #AE78BE;
}
```

**ფონის სურათი**ს არჩევა მისამართიდან:
```css
{
    background: url(https://www.17thshard.com/forum/uploads/monthly_2018_10/Silmarillion_Tuor1.jpg.6200bf9c97e8100f9dddbbcddbd98f23.jpg);
}
```
პარამეტრი | მნიშვნელობა
--- | ---
background-repeat | no-repeat

### ჩარჩო


```css
div{
    background: maroon;
    border: orange;
    border-width: thick;
    border-style: dotted;
}
```
ან
```css
div{
    background: maroon;
    border: royalblue 2px dashed;
}
```

### ფონტი
#### ჩაშენებული ფონტების გამოყენება
```css
p {
  font-family: verdana;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
}
```
#### ვებ-ფონტების გამოყენება
