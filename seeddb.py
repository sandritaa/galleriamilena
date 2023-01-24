import crud
from model import db

db.session.add(crud.create_artist_profile('Shirin', 'Haghi', 'shirin@gmail.com', 'testtest', 'Persia', 'shirin',
               'I am a young Persian artist, with a passion for drawing mandalas. I specialize in traditional Persian patterns and symbols, and my intricate works evoke reflection and introspection. I am constantly pushing the boundaries of mandala art and exploring new possibilities in this meditative art form. I am excited to share my art with the world and see where my talent will take me in the future.', 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674006183/s1_w9pcma.jpg'))
db.session.commit()
db.session.add(crud.create_artist_profile('Silvia', 'Brogi', 'silvia@gmail.com', 'testtest', 'Italy', 'silvia', 'I am an Italian artist who loves to paint rocks and transform them into unique characters during my free time. I find inspiration in nature and aim to create whimsical and imaginative pieces. My rock paintings have a strong sense of storytelling and are meant to delight both adults and children. I am constantly experimenting with new techniques and materials during my free time, and I am excited to see where my art will take me next.', 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674004760/bbf6ebc6-8b16-462e-8fd0-24b22419d7b6_uzrgzs.jpg'))
db.session.commit()
db.session.add(crud.create_artist_profile('Antonello', 'Rossi', 'antonello@gmail.com', 'testtest', 'South Africa', 'antonello', 'As a long-term artist from South Africa, I have been painting for many years, honing my skills and developing my style. I specialize in oil paintings and am known for my use of vibrant colors. I draw inspiration from the diverse landscapes and cultures of my country, and I strive to capture the essence of South Africa in my paintings. My work has been exhibited in galleries and art fairs around the world and I am proud to have my paintings in private collections globally. I continue to push my boundaries and evolve as an artist.', 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674009959/IMG_4237_ujp7tt.jpg'))
db.session.commit()
db.session.add(crud.create_artist_profile('Camila', 'Orpen', 'camila@gmail.com', 'testtest', 'France', 'jannel',
               'Born in Paris on May 12th, 1959, I studied at the Polimoda in Florence, Italy. I specialize in creating art using oil on canvas. I enjoy exploring different themes and styles in my work, and am always seeking new ways to express myself through my paintings.', 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674504474/4-1_tvkisg.png'))
db.session.commit()
db.session.add(crud.create_artist_profile('Marta', 'Cecilia', 'antonello@gmail.com', 'testtest', 'Colombia', 'marta',
               'Colombian artist who likes to use mixed media on canvas to create unique and expressive pieces. My work often combines traditional techniques with modern materials to create a dynamic visual language. I am constantly exploring new ways to express myself through art and am always looking for new inspiration.', 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674504985/5-1_sojy1z.png'))
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

db.session.add(crud.create_item('pede posuere nonummy integer non velit donec diam neque vestibulum eget vulputate ut ultrices vel augue vestibulum ante ipsum primis in fauc',
               '16x16',  30.0, '12/7/2022', 'green', True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674006183/s1_w9pcma.jpg', 1))
db.session.commit()
db.session.add(crud.create_item('hac habitasse platea dictumst aliquam augue quam sollicitudin vitae consectetuer eget rutrum at lorem integer tincidunt ante vel ipsum praes',
               '20x20', 45.00, '8/30/2022', 'black',  True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674006183/s2_xcj7gu.jpg', 1))
db.session.commit()
db.session.add(crud.create_item('morbi a ipsum integer a nibh in quis justo maecenas rhoncus aliquam lacus morbi quis tortor id Nonea ultrices aliquet maecenas leo odio cond',
               '10x10', 25.00, '4/24/2022', 'red',    True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674006183/s4_pnfdae.jpg', 1))
db.session.commit()
db.session.add(crud.create_item('sit amet erat Nonea tempus vivamus in felis eu sapien cursus vestibulum proin eu mi Nonea ac enim in tempor turpis nec euismod scelerisque q',
               '6x10', 20.00, '2/7/2022', 'red',     True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674004760/bbf6ebc6-8b16-462e-8fd0-24b22419d7b6_uzrgzs.jpg', 2))
db.session.commit()
db.session.add(crud.create_item('pede libero quis orci Noneam molestie nibh in lectus pellentesque at Nonea suspendisse potenti cras in purus eu magna vulputate luctus cum s',
               '10x10',  20.00,  '7/6/2022', 'gray',    True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1673735759/eqb6g9ohus9fdbltjhkk.jpg', 2))
db.session.commit()
db.session.add(crud.create_item('semper sapien a libero nam dui proin leo odio porttitor id consequat in consequat ut Nonea sed accumsan felis ut at dolor quis odio consequ',
               '8x10',   20.00, '5/12/2022', 'green',  True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1673229395/e63209a8-ebda-4ecc-acca-4ac86aa98e8b_juvnyu.jpg', 2))
db.session.commit()
db.session.add(crud.create_item('tellus in sagittis dui vel nisl duis ac nibh fusce lacus purus aliquet at feugiat non pretium quis lectus suspendisse potenti in eleifend qu',
               '20x12', 95.77, '8/12/2022', 'red',    True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1673229399/FullSizeRender_c3qqdu.jpg', 3))
db.session.commit()
db.session.add(crud.create_item('tristique est et tempus semper est quam pharetra magna ac consequat metus sapien ut nunc vestibulum ante ipsum primis in faucibus orci luctu',
               '45x45',   83.00, '7/2/2022', 'blue',    True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674009959/IMG_4237_ujp7tt.jpg', 3))
db.session.commit()
db.session.add(crud.create_item('pede posuere nonummy integer non velit donec diam neque vestibulum eget vulputate ut ultrices vel augue vestibulum ante ipsum primis in fauc',
               '30x45',  74.00, '12/7/2022', 'green',  True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674009959/IMG_0458_i1jhob.jpg', 3))
db.session.commit()
db.session.add(crud.create_item('hac habitasse platea dictumst aliquam augue quam sollicitudin vitae consectetuer eget rutrum at lorem integer tincidunt ante vel ipsum praes',
               '110x220', 50.00, '8/30/2022', 'black',  True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674504475/4-5_ndrppf.png', 4))
db.session.commit()
db.session.add(crud.create_item('hac habitasse platea dictumst aliquam augue quam sollicitudin vitae consectetuer eget rutrum at lorem integer tincidunt ante vel ipsum praes',
               '160x220', 63.81, '8/30/2022', 'black',  True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674504474/4-1_tvkisg.png', 4))
db.session.commit()
db.session.add(crud.create_item('hac habitasse platea dictumst aliquam augue quam sollicitudin vitae consectetuer eget rutrum at lorem integer tincidunt ante vel ipsum praes',
               '198x162', 250.00, '8/30/2022', 'black',  True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674504475/4-3_cg0zc0.png', 4))
db.session.commit()
db.session.add(crud.create_item('hac habitasse platea dictumst aliquam augue quam sollicitudin vitae consectetuer eget rutrum at lorem integer tincidunt ante vel ipsum praes',
               '150x11', 90.00, '8/30/2022', 'black',  True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674504985/5-1_sojy1z.png', 5))
db.session.commit()
db.session.add(crud.create_item('aenean lectus pellentesque eget nunc donec quis orci eget orci vehicula condimentum curabitur in libero ut massa volutpat convallis morbi od',
               '150x16', 75.00, '1/18/2022', 'purple', True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674504986/5-2_oz6lt5.png', 5))
db.session.commit()
db.session.add(crud.create_item('eleifend donec ut dolor morbi vel lectus in quam fringilla rhoncus mauris enim leo rhoncus sed vestibulum sit amet cursus id turpis integer ',
               '33x37x3,5', 100.00, '1/2/2022', 'yellow',  True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674504986/5-3_qdyc8u.png', 5))
db.session.commit()
db.session.add(crud.create_item('morbi a ipsum integer a nibh in quis justo maecenas rhoncus aliquam lacus morbi quis tortor id Nonea ultrices aliquet maecenas leo odio cond',
               '150x115', 51.00, '4/24/2022', 'red',    True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674505245/6-3_acomuf.png', 6))
db.session.commit()
db.session.add(crud.create_item('sit amet erat Nonea tempus vivamus in felis eu sapien cursus vestibulum proin eu mi Nonea ac enim in tempor turpis nec euismod scelerisque q',
               '115x70', 63.00, '2/7/2022', 'red',     True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674505245/6-4_wcnfom.png', 6))
db.session.commit()
db.session.add(crud.create_item('sit amet erat Nonea tempus vivamus in felis eu sapien cursus vestibulum proin eu mi Nonea ac enim in tempor turpis nec euismod scelerisque q',
               '50x30', 90.00, '2/7/2022', 'red',     True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674505245/6-2_lvhihh.png', 6))
db.session.commit()
db.session.add(crud.create_item('tellus in sagittis dui vel nisl duis ac nibh fusce lacus purus aliquet at feugiat non pretium quis lectus suspendisse potenti in eleifend qu',
               '150x11', 95.77, '8/12/2022', 'red', True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674504977/5-4_z9mvyh.png', 5))
db.session.commit()
db.session.add(crud.create_item('tristique est et tempus semper est quam pharetra magna ac consequat metus sapien ut nunc vestibulum ante ipsum primis in faucibus orci luctu',
               '4x4',   12.45, '7/2/2022', 'blue', True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674006183/s5_ehuvpn.jpg', 1))
db.session.commit()
db.session.add(crud.create_item('aenean lectus pellentesque eget nunc donec quis orci eget orci vehicula condimentum curabitur in libero ut massa volutpat convallis morbi od',
               '30x45', 79.43, '1/18/2022', 'purple', True,  'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674006183/s6_dpgaur.jpg', 1))
db.session.commit()
db.session.add(crud.create_item('eleifend donec ut dolor morbi vel lectus in quam fringilla rhoncus mauris enim leo rhoncus sed vestibulum sit amet cursus id turpis integer ',
               ' 50x30', 67.14, '1/2/2022', 'yellow',  True, 'https://res.cloudinary.com/dxsxg4nkp/image/upload/v1674505245/6-1_dkoosx.png', 6))
db.session.commit()
