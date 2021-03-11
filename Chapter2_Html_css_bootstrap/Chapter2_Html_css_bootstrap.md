# [HTML Introduction](https://www.w3schools.com/html/html_intro.asp)

HTML არის მარკირების ენა რომელიც გამოიყენება ვებ გვერდების შესაქმნელად.

HTML ტიპის ფაილებს აქვთ `.html` გაფართოება. გაფართოება მიანიშნებს ტექსტურ ედიტორს
ან ვებ ბრაუზერს მიხვდეს თუ რა ტიპის ფაილთან აქვს ურთიერთობა. ახალი html
ფაილის შექმნისას ის უნდა შევინახოთ შესაბამის ფორმატში.

მაგალითად: `main.html`

ამ ფაილის გახსნისას ბრაუზერს ეცოდინება როგორ გამოიტანოს მასში მოთავსებული html კოდი.

## სტრუქტურა

თანამედროვე ინტეგრირებული გარემოების (IDLE) უმრავლესობას, როგორიც არის PyCharm, WebStorm, Atom და ა.შ. აქვს ჩაშენებული საწყისი HTML-ის შაბლონი.

HTML დოკუმენტის სტრუქტურა მოიცავს ორ ბლოკს `<head> </head>` და `<body> </body>`.

- head ბლოკში გაერთიანებული ელემენტები გამოიყენება html დოკუმენტის აღწერისთვის და კონფიგურაციისთვის. იგი ვებგვერდზე არ ჩანს ვიზუალურად და ინახავს meta ინფორმაციას, დაკავშირებულ ფაილებს, ენკოდინგის ტიპს და ა.შ. მაგ: `<title> Title </title>`

- body ბლოკში გაერთიანებული ელემენტები გამოიყენება ვიზუალური მხარის შესაქმნელად. მაგ: `<p> Hello world </p>`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <p>Hello world</p>
  </body>
</html>
```

## HTML ელემენტების სტრუქტურა

\_[მსგავსება HTML-სა და Markdown ფორმატ შორის და ასევე უამრავი საჭირო თეგი თავისი მაგალითებით შეგიძლიათ ნახოთ ამ მისამართზე](https://www.markdownguide.org/basic-syntax/)

![html თეგები](./images/elementStructure.png)

### Div და Span

Div და Span გვეხმარება html კოდის პორციებად დაყოფაში. როდესაც დავიწყებთ ელემენტებისთვის სტილის მინიჭებას, ხშირად გვექნება შემთხვევა როდესაც გარკვეული სტილის
გამოყენება მხოლოდ კონკრეტული ელემენტების სეგმენტზე გვჭირდება. ასეთი შემთხვევებისთვის გამოიყენება ეს თეგები.

### სინტაქსი:

```html
...

<div class="container">
  <h1>სათაური</h1>
  <p>პარაგრაფი</p>
</div>
<p>პარაგრაფი div-ის გარეთ რომელიც <span>span თეგს შორის</span> მოვათავსეთ</p>

...
```

## ტექსტი, პარაგრაფი, ფორმატირება

### სათაურები

```html
<h1>პირველი დონის სათაური</h1>
...
<h6>მეექვსე დონის სათაური</h6>
```

| თეგი   | ელემენტი             |
| ------ | -------------------- |
| **h1** | მაღალი დონის სათაური |
| **h6** | დაბალი დონის სათაური |

### პარაგრაფები

```html
<p>
  პარაგრაფი.<br />
  ახალი ხაზი.
</p>
<p>ახალი პარაგრაფი.</p>
<hr />
<p>ნახეთ ხაზი ზემოთ.</p>
```

| თეგი   | ელემენტი           |
| ------ | ------------------ |
| **p**  | პარაგრაფი          |
| **br** | ახალი ხაზი         |
| **hr** | ჰორიზონტალური ხაზი |

### ტექსტის ფორმატირება

```html
<em>Formatting</em> is <strong>important</strong> ! (a+b)
<sup
  >2<sup> = a<sup>2</sup>+ b<sup>2</sup> + 2ab</sup></sup
>
```

| თეგი       | ელემენტი    |
| ---------- | ----------- |
| **sub**    | subscript   |
| **sup**    | superscript |
| **em**     | emphasize   |
| **strong** | important   |
| **mark**   | highlighted |
| **small**  | small       |
| **i**      | italic      |
| **b**      | bold        |

## ატრიბუტები

ზოგ HTML ელემენტს გააჩნია ატრიბუტები, ატრიბუტები განსაზღვრავენ ელემენტის რაობას.
შესაბამისი ატრიბუტების გამოყენებით შეგვიძლია ელემენტს მივანიჭოთ სტილი, ბმული, სახელი და ა.შ

### ბმულები

```html
<a href="url">გახსენი ბმული იმავე ფანჯარაში</a>
<a href="url" target="_blank">გახსენი ბმული ახალ ფანჯარაში</a>

<a href="#comments">ბმული ელემენტზე id-ით კომენტარი</a>
<h2 id="comments">კომენტარი</h2>
```

| ატრიბუტი | აღწერა           |
| -------- | ---------------- |
| **href** | ბმულის მისამართი |

### სურათები

```html
<img
  src="https://www.flixist.com/wp-content/uploads/ul/226276-midnightgospel1.jpg"
  alt="description"
  width="300"
  height="200"
/>
```

| თეგი    | ელემენტი |
| ------- | -------- |
| **img** | image    |

| ატრიბუტი      | აღწერა          |
| ------------- | --------------- |
| src           | მისამართი       |
| alt           | ტექსტი          |
| width; height | სიგანე; სიმაღლე |

## [ფორმები](https://www.w3schools.com/html/html_forms.asp)

ვებ გვერდის ერთ-ერთი უმნიშვნელოვანეს ფუნქციონალია მომხმარებლისგან ინფორმაციის აღება. ინფორმაციის
ვებ გვერდის ინტერფეისიდან ამოღება ხდება html ფორმების გამოყენებით. ფორმის ასაწყობად ვიყენებთ
html თეგს `<form>`, რომელშიც შეგვიძლია მოვათავსოთ `<input>` ელემენტი.

ფორმის დასასრულს ვამატებთ **submit** ტიპის input-ს, რაც ავტომატურად ამაგრებს ღილაკს შევსებული ფორმის შესასრულებლად.

```html
<form>
  <fieldset>
    <legend>რეგისტრაცია</legend>
    <label for="signIn">სახელი :</label>
    <input type="text" id="signIn" name="login" />
    <br />
    <label for="pswd">პაროლი :</label>
    <input type="password" name="password" id="pswd" />

    <br />
    <label>სქესი:</label>
    <br />
    <input type="radio" name="sex" value="male" />მამრობითი<br />
    <input type="radio" name="sex" value="female" />მდედრობითი<br />
    <br />

    <label>საყვარელი პოკემონი : </label>
    <select name="color">
      <option>Charizard</option>
      <option>Gengar</option>
      <option>Greninja</option>
    </select>
    <br />

    <br />
    <input type="checkbox" name="" id="robot" />
    <label for="robot">არ ვარ რობოტი</label>
    <br />
    <input type="checkbox" name="" id="rules" />
    <label for="rules">ვეთანხმები ვებგვერდის წესებს</label>
    <br />

    <br />
    <textarea
      name=""
      id=""
      cols="30"
      rows="10"
      placeholder="კომენტარის სივრცე"
    ></textarea>

    <br />
    <input type="submit" value="რეგისტრაცია" />
  </fieldset>
</form>
```

| თეგი                        | ელემენტი                      |
| --------------------------- | ----------------------------- |
| **form**                    | form                          |
| **label**                   | label for input               |
| **fieldset**                | group inputs together         |
| **legend** for=""           | legend for fieldset           |
| **input** type="_text_"     | text input                    |
| **input** type="_password_" | password input                |
| **input** type="_radio_"    | radio button                  |
| **input** type="_checkbox_" | checkbox                      |
| **input** type="_submit_"   | send form                     |
| **select**                  | drop-down list                |
| **option**                  | drop-down list item           |
| **optgroup**                | group of drop-down list items |
| **datalist**                | autocompletion list           |
| **textarea**                | large text input              |

## ხშირად გამოყენებადი თეგები

### დაუნომრავი სია

```html
<ul>
  <li>item</li>
  <li>item</li>
  <li>item</li>
</ul>
```

| თეგი   | ელემენტი       |
| ------ | -------------- |
| **ul** | unordered list |
| **li** | list item      |

### დანომრილი სია (დალაგებული)

```html
<ol>
  <li>first</li>
  <li>second</li>
  <li>third</li>
</ol>
```

| თეგი   | ელემენტი     |
| ------ | ------------ |
| **ol** | ordered list |
| **li** | list item    |

### სტანდარტული ცხრილი

```html
<table>
  <tr>
    <th>სათაური 1</th>
    <th>სათაური 2</th>
  </tr>
  <tr>
    <td>მწკრივი 1, სვეტი 1</td>
    <td>მწკრივი 1, სვეტი 2</td>
  </tr>
  <tr>
    <td>მწკრივი 2, სვეტი 1</td>
    <td>მწკრივი 2, სვეტი 2</td>
  </tr>
</table>
```

| თეგი      | ელემენტი           |
| --------- | ------------------ |
| **table** | ცხრილი             |
| **tr**    | ცხრილის მწკრივი    |
| **th**    | ცხრილის დასახელება |
| **td**    | ცხრილის უჯრა       |

# css

**cascading style sheets** ( CSS ) აღწერს თუ როგორ გამოჩნდება HTML ელემენტები ვებ გვერდზე.
CSS შეუძლია რამოდენიმე სხვადასხვა გვერდზე განლაგებულ ელემენტებზე იქონიოს გავლენა. სტილის დაწერა შეგვიძლია თვითონ html დოკუმენტში, კონკრეტულ html ელემენტზე და დაკავშირებულ ფაილში, მაგ.: `style.css`

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

## css სტრუქტურა

![ანატომია](https://mdn.mozillademos.org/files/9461/css-declaration-small.png)

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

# [Bootstrap4](https://getbootstrap.com/)

### [შესავალი](https://getbootstrap.com/docs/4.5/getting-started/introduction/) | [მაგალითები](https://getbootstrap.com/docs/4.5/examples/) | [დოკუმენტაცია](https://getbootstrap.com/docs/4.5/layout/overview/)

Boostrap არის მსოფლიოში ერთ-ერთი ყველაზე პოპულარული ფრონტ-ენდ დეველოპმენტ იარაღების ნაკრები. იგი შექმნეს twitter -ის დეველოპერებმა. მას აქვს html ელემენტების და css სტილის მზა შაბლონები.

## როგორ გამოვიყენოთ Bootstrap

არსებობს Bootstrap-ის პროექტში ჩაშენების რამოდენიმე გზა.

- თქვენ შეგიძლიათ ინდივიდუალურად [გადმოწეროთ Bootstrat](https://getbootstrap.com/docs/4.5/getting-started/download/)
  სორს კოდთან და კომპონენტებთან ერთად.
- დააყენოთ რომელიმე სასურველი Package Manager-ის მეშვეობით (npm, yarn, RubyGems, NuGet, Composer).
- შემოიტანოთ შესაბამისი ბმულები html ფაილში, [BootstrapCDN](https://www.bootstrapcdn.com/) ის მეშვეობით.

### cdn -ით დაყენება

```html
<!-- in head section -->
<!-- CSS only -->
<link
  rel="stylesheet"
  href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
  integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z"
  crossorigin="anonymous"
/>

<!-- at the end of the body section -->
<!-- JS, Popper.js, and jQuery -->
<script
  src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
  integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
  crossorigin="anonymous"
></script>
<script
  src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"
  integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN"
  crossorigin="anonymous"
></script>
<script
  src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"
  integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV"
  crossorigin="anonymous"
></script>
```

## [bootstrap სტილი](https://getbootstrap.com/docs/4.5/layout/overview/)

bootstrap სტილის გამოყენებისთვის სასურველ html ელემენტს უნდა მივანიჭოთ bootstrap class-ი.

```html
<button type="button" class="btn btn-primary">Primary</button>
```

## [კომპონენტები](https://getbootstrap.com/docs/4.5/components/)

**კომპონენტი** Bootstrap-ში წინასწარ გამზადებული ვებ-გვერდის შაბლონია.

### [navbar](https://getbootstrap.com/docs/4.5/components/navbar/)

თანამედროვე ვებ გვერდის მნიშვნელოვან ატრიბუტს წარმოადგენს navbar - სანავიგაციო ზოლი. ბუტსტრეპის ნავბარები არის რესპონსივ ელემენტები რაც ნიშნავს რომ ის ავტომატურად იცვლის ზომას ან ფორმას
ეკრანის ტიპისა და გაფართოების გათვალისწინებით.

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button
    class="navbar-toggler"
    type="button"
    data-toggle="collapse"
    data-target="#navbarNavAltMarkup"
    aria-controls="navbarNavAltMarkup"
    aria-expanded="false"
    aria-label="Toggle navigation"
  >
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
    <div class="navbar-nav">
      <a class="nav-link active" href="#"
        >Home <span class="sr-only">(current)</span></a
      >
      <a class="nav-link" href="#">Features</a>
      <a class="nav-link" href="#">Pricing</a>
      <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true"
        >Disabled</a
      >
    </div>
  </div>
</nav>
```

## დამატებითი რესურსები

1. [HTML-ის დოკუმენტაცია](https://developer.mozilla.org/en-US/docs/Web/HTML)
2. [css -ის დოკუმენტაცია](https://developer.mozilla.org/en-US/docs/Web/css)
3. [Bootstrap -ის დოკუმენტაცია](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
