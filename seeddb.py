import crud
db.create_all()


db.session.add(crud.create_artist_profile('Shirin', 'Haghi', 'shirin@gmail.com', 'testtest', 'Persia', 'shirin',
               'I am a young Persian artist, with a passion for drawing mandalas. I specialize in traditional Persian patterns and symbols, and my intricate works evoke reflection and introspection. I am constantly pushing the boundaries of mandala art and exploring new possibilities in this meditative art form. I am excited to share my art with the world and see where my talent will take me in the future.', 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674006183/s1_w9pcma.jpg'))
db.session.commit()
db.session.add(crud.create_artist_profile('Marta', 'Cecilia', 'antonello@gmail.com', 'testtest', 'Colombia', 'marta',
               'Colombian artist who likes to use mixed media on canvas to create unique and expressive pieces. My work often combines traditional techniques with modern materials to create a dynamic visual language. I am constantly exploring new ways to express myself through art and am always looking for new inspiration.', 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674504985/5-1_sojy1z.png'))
db.session.commit()
db.session.add(crud.create_artist_profile('Antonello', 'Rossi', 'antonello@gmail.com', 'testtest', 'South Africa', 'antonello', 'As a long-term artist from South Africa, I have been painting for many years, honing my skills and developing my style. I specialize in oil paintings and am known for my use of vibrant colors. I draw inspiration from the diverse landscapes and cultures of my country, and I strive to capture the essence of South Africa in my paintings. My work has been exhibited in galleries and art fairs around the world and I am proud to have my paintings in private collections globally. I continue to push my boundaries and evolve as an artist.', 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674009959/IMG_4237_ujp7tt.jpg'))
db.session.commit()
db.session.add(crud.create_artist_profile('Camila', 'Orpen', 'camila@gmail.com', 'testtest', 'France', 'jannel',
               'Born in Paris on May 12th, 1959, I studied at the Polimoda in Florence, Italy. I specialize in creating art using oil on canvas. I enjoy exploring different themes and styles in my work, and am always seeking new ways to express myself through my paintings.', 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674504474/4-1_tvkisg.png'))
db.session.commit()
db.session.add(crud.create_artist_profile('Silvio', 'Brogi', 'silvio@gmail.com', 'testtest', 'Italy', 'silvio',
               ' In 1960 he began to exhibit in Pistoia and Florence. The works were paintings, photographs, casts, sculptures and topographies which he also presented in Rome in 1963. It was in Rome that he met Cesare Vivaldi, who in 1965 invited him to Revort/1, a show organised as part of the ‘gruppo 63’ festival in Palermo. ', 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674762490/7-1_rsg8ti.png'))
db.session.commit()
db.session.add(crud.create_artist_profile('Laura', 'Jane', 'laura@gmail.com', 'testtest', 'Italy', 'laura',
               'I am a Milan-based artist, working with various media such as photography, performance, video and installation to explore the concepts of history and memory. My approach is provocative and I always play on the thin border between irony and parody, between displacement and visual and semantic detournement. I specialize in print on glass and mirror.', 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674505245/6-2_lvhihh.png'))
db.session.commit()
db.session.add(crud.create_customer_profile(
    'John', 'Doe', 'john@gmail.com', '990-165-0100', 'testtest'))
db.session.commit()
db.session.add(crud.create_customer_profile('Jane', 'Smith',
               'jane@gmail.com', '268-342-8970', 'testtest'))
db.session.commit()
db.session.add(crud.create_customer_profile('Bertullio', 'Tomide',
               'bertullio@gmail.com', '246-589-8124', 'testtest'))
db.session.commit()


db.session.add(crud.create_item('This mandala art piece is created with vibrant hues of blue, green, and yellow using fine-tipped markers and a compass for precision geometric shapes.',
               '16x16',  30.0, '12/7/2022', 'Green', True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674006183/s1_w9pcma.jpg', 1))
db.session.commit()
db.session.add(crud.create_item('Handpainted mandala art with a vibrant color palette and intricate patterns created using fine brushwork for a mesmerizing and harmonious masterpiece',
               '20x20', 45.00, '8/30/2022', 'Blue',  True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674006183/s2_xcj7gu.jpg', 1))
db.session.commit()
db.session.add(crud.create_item('Elegant handpainted mandala art with a subtle color palette and delicate patterns created using a fine brush and ink for a serene masterpiece',
               '10x10', 25.00, '4/24/2022', 'Red',    True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674006183/s4_pnfdae.jpg', 1))
db.session.commit()
db.session.add(crud.create_item('Intricate handpainted mandala art featuring a harmonious blend of colors and patterns crafted using traditional persian painting techniques',
               '24x24',   40.00, '7/2/2022', 'Black', True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674006183/s5_ehuvpn.jpg', 1))
db.session.commit()
db.session.add(crud.create_item('Handpainted mandala art with bold hues and geometric patterns created using stencils and a variety of mark-making tools for a striking visual impact"',
               '30x45', 30.00, '1/18/2022', 'Turquoise', True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674006183/s6_dpgaur.jpg', 1))
db.session.commit()
db.session.add(crud.create_item('This mandala art piece is created with vibrant hues of blue, gold, and red using fine-tipped markers and a compass for precision geometric shapes.',
               '40x40', 80.00, '1/18/2022', 'Blue', True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674795796/IMG_4443_ipfofg.jpg', 1))
db.session.commit()

db.session.add(crud.create_item('Vibrant mixed media canvas w/ intricate patterns crafted using stencils, spray paint, & a variety of mark making tools.',
               '150x11', 90.00, '8/30/2022', 'Orange',  True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674504985/5-1_sojy1z.png', 2))
db.session.commit()
db.session.add(crud.create_item('Mixed media canvas featuring bold patterns created with layering, collage & textured tools for a dynamic, abstract masterpiece',
               '150x16', 75.00, '1/18/2022', 'Pink', True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674504986/5-3_qdyc8u.png', 2))
db.session.commit()
db.session.add(crud.create_item('Elegant oil painting, featuring a harmonious blend of muted colors and subtle brushstrokes for a timeless and sophisticated masterpiece.',
               '150x11', 95.77, '8/12/2022', 'Orange', True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674504977/5-4_z9mvyh.png', 2))
db.session.commit()
db.session.add(crud.create_item('Mixed media canvas with patterns crafted using stencils, spray paint, and a variety of mark making tools.',
               '33x37', 100.00, '1/2/2022', 'Blue',  True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674504986/5-2_oz6lt5.png', 2))
db.session.commit()
db.session.add(crud.create_item('Rich oil painting featuring bold hues & organic patterns created with palette knife & brushstrokes for a dynamic, textured masterpiece.',
               '20x12', 95.77, '8/12/2022', 'Red',    True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674763401/IMG_0407_dgiglt.png', 3))
db.session.commit()
db.session.add(crud.create_item('Vibrant oil painting with bold colors and intricate patterns crafted using impasto and palette knife techniques for a striking visual impact.',
               '45x45',   83.00, '7/2/2022', 'Multi',    True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674009959/IMG_4237_ujp7tt.jpg', 3))
db.session.commit()
db.session.add(crud.create_item('Luminous oil painting with a harmonious blend of colors & patterns created using layering & brushstrokes for a serene, ethereal masterpiece.',
               '30x45',  74.00, '12/7/2022', 'Blue',  True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674763401/IMG_0435_c6yik0.png', 3))
db.session.commit()
db.session.add(crud.create_item('Luminous oil painting with a harmonious blend of colors & patterns created using layering & brushstrokes for a serene, ethereal masterpiece.',
               '110x220', 50.00, '8/30/2022', 'Black',  True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674504475/4-5_ndrppf.png', 4))
db.session.commit()
db.session.add(crud.create_item('Rich oil painting featuring bold hues & organic patterns created with palette knife & brushstrokes for a dynamic, textured masterpiece',
               '160x220', 63.81, '8/30/2022', 'Green',  True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674504474/4-1_tvkisg.png', 4))
db.session.commit()
db.session.add(crud.create_item('Vibrant oil painting with bold colors & intricate patterns crafted using impasto and palette knife techniques for a striking visual impact.',
               '198x162', 250.00, '8/30/2022', 'Red',  True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674504475/4-3_cg0zc0.png', 4))
db.session.commit()
db.session.add(crud.create_item('Elegant oil painting, featuring a harmonious blend of muted colors and subtle brushstrokes for a timeless and sophisticated masterpiece.',
               '6x10', 20.00, '2/7/2022', 'Red',     True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674762490/7-1_rsg8ti.png', 5))
db.session.commit()
db.session.add(crud.create_item('Luminous oil painting with a harmonious blend of colors & patterns created using layering & brushstrokes for a serene, ethereal masterpiece.',
               '10x10',  20.00,  '7/6/2022', 'Black',    True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674762490/7-3_k7stuv.png', 5))
db.session.commit()
db.session.add(crud.create_item('Expressive oil painting, featuring a vibrant color palette and bold brushstrokes for a dynamic and textured masterpiece',
               '8x10',   20.00, '5/12/2022', 'Yellow',  True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674762490/7-2_cqggh5.png', 5))
db.session.commit()
db.session.add(crud.create_item('Rich oil painting featuring bold hues & organic patterns created with palette knife & brushstrokes for a dynamic, textured masterpiece',
               '8x10',   20.00, '5/12/2022', 'Black',  True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674762490/7-4_mw3vz5.png', 5))
db.session.commit()
db.session.add(crud.create_item('Luminous painting with a harmonious blend of colors & patterns created using layering & brushstrokes for a serene, ethereal masterpiece.',
               '150x115', 51.00, '4/24/2022', 'Orange',    True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674505245/6-3_acomuf.png', 6))
db.session.commit()
db.session.add(crud.create_item('Expressive oil painting, featuring a vibrant color palette and bold brushstrokes for a dynamic and textured masterpiece',
               '115x70', 63.00, '2/7/2022', 'Green',     True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674505245/6-4_wcnfom.png', 6))
db.session.commit()
db.session.add(crud.create_item('Oil painting with a harmonious blend of warm and cool colors, created using layering and palette knife techniques for a striking visual impact.',
               '50x30', 90.00, '2/7/2022', 'Purple',     True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674505245/6-2_lvhihh.png', 6))
db.session.commit()

db.session.add(crud.create_item('Rich oil painting featuring bold hues & organic patterns created with palette knife & brushstrokes for a dynamic, textured masterpiece',
               ' 50x30', 67.14, '1/2/2022', 'Red',  True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674505245/6-1_dkoosx.png', 6))
db.session.commit()
