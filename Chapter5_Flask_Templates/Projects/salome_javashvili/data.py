pathogens = ['Bacteria', 'Virus', 'Fungi', 'Parasite']
pathogens_ge = ['ბაქტერია', 'ვირუსი', 'სოკო', 'პარაზიტი']


regions = ['Tbilisi', 'Kakheti', 'Inner Kartli', 'Lower Kartli', 'Mtskheta-Mtianeti', 'Imereti',
           'Samegrelo-Upper Svaneti', 'Ratcha-Lechkhumi/ Lower Svaneti', 'Samtskhe-Javakheti', 'Guria', 'Adjara']

regions_ge = ['თბილისი', 'კახეთი', 'შიდა ქართლი', 'ქვემო ქართლი', 'მცხეთა-მთიანეთი', 'იმერეთი',
              'სამეგრელო-ზემო სვანეთი', 'რაჭა-ლეჩხუმი/ ქვემო სვანეთი', 'სამცხე-ჯავახეთი', 'გურია', 'აჭარა']


select_menu_keys = ['_id', 'label', 'options_list', 'option_selected']

select_menu_values = [("inputRegion", "Region", regions, 'Georgia'),
                      ("inputDate1", "From:", [i for i in range(2001, 2022)], 2000),
                      ("inputDate2", "To:", [i for i in range(2000, 2021)], 2021)
                      ]

select_menu_values_ge = [("inputRegion", "რეგიონი", regions_ge, 'საქართველო'),
                         ("inputDate1", "როდიდან:", [i for i in range(2001, 2022)], 2000),
                         ("inputDate2", "როდემდე:", [i for i in range(2000, 2021)], 2021)
                         ]

input_form_keys = ['_id', 'label', 'placeholder']

input_form_values = [('Genus', 'Genus', 'e.g. Staphylococcus'),
                     ('Species', 'Species', 'e.g. S. aureus'),
                     ('Strain', 'Strain', 'e.g. S. MRSA')
                     ]

input_form_values_ge = [('Genus', 'გვარი', 'მაგ. Staphylococcus'),
                     ('Species', 'სახეობა', 'მაგ. S. aureus'),
                     ('Strain', 'შტამი', 'მაგ. S. MRSA')
                     ]