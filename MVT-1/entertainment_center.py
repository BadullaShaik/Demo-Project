import media
import fresh_tomatoes

ChittiChilakamma=media.Movie("Chitti Chilakamma",
                             "Chitti Chilakamma - Parrots 3D Animation Telugu Rhymes For children with lyrics",
                             "https://i.ytimg.com/vi/pFqzNePraJg/maxresdefault.jpg",
                             "https://www.youtube.com/watch?v=-IPKPz1pujM")

Chalo_story=media.Movie("Chalo","Chalo Trailer | Naga Shaurya, Rashmika Mandanna | Ira Creations | Theatrical Trailer",
                    "http://www.ratingdada.com/images/3/11222017115115am_chalo.jpg",
                    "https://www.youtube.com/watch?v=6_BxEjvWsqs")
#print(toy_story.storyline)

katamraudu=media.Movie("Katamrayudu",
                       "It is Beautuful love song",
                       "http://mananela.com/wp-content/uploads/2016/12/Katamarayudu.jpg",
                       "https://www.youtube.com/watch?v=zggQw2wb60M")
Nartanasala=media.Movie("Nartanasala",
                        "Narthanasala Teaser || Narthanasala Movie Latest Trailer || Naga Shaurya, Kashmira, Yamini || 2018",
                        "https://i.ytimg.com/vi/uY4pp0mgpmc/maxresdefault.jpg",
                        "https://www.youtube.com/watch?v=uY4pp0mgpmc")
Geetha_govindam=media.Movie("Geetha Govindam",
                            "Geetha Govindam ReleaseTrailer || Vijay Devarakonda||Rithika||Fan Made",
                            "https://akm-img-a-in.tosshub.com/indiatoday/images/story/201808/Geetha_Govindam_3.jpeg?lViC8c3iiHCmONeSNIQ9waMy4RbtVFou",
                            "https://www.youtube.com/watch?v=UVqbymdrLGs")

#print(katamraudu.storyline)

#katamraudu.show_trailer()

movies=[ChittiChilakamma,Chalo_story,katamraudu,Nartanasala,Geetha_govindam]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
