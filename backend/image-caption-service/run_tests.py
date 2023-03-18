import unittest
from main import GetImageCaption


class TestStringMethods(unittest.TestCase):
    def test_caption_cow(self):
        img_src = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/a64e2c60-f1b6-4851-a3eb-ced3dad5a85c/drb2pe-b2dece91-ec62-4d99-9ce9-32dc8a427b61.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2E2NGUyYzYwLWYxYjYtNDg1MS1hM2ViLWNlZDNkYWQ1YTg1Y1wvZHJiMnBlLWIyZGVjZTkxLWVjNjItNGQ5OS05Y2U5LTMyZGM4YTQyN2I2MS5qcGcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.KtVQfMRlrkzivq_jO0oySyo9wwoQYIefHONewp3k73I"
        result = GetImageCaption(img_src)
        expected_result = "a cow licking a flower"
        if not result:
            self.fail("No caption generated")
        self.assertEqual(result.get("result"), expected_result)

    def test_caption_person(self):
        img_src = "https://img.freepik.com/premium-photo/man-with-washcloth-cleaning-floor-apartment_85574-1160.jpg"
        result = GetImageCaption(img_src)
        expected_result = "a person cleaning a floor"
        if not result:
            self.fail("No caption generated")
        self.assertEqual(result.get("result"), expected_result)

    def test_caption_car(self):
        img_src = "https://images.unsplash.com/photo-1494976388531-d1058494cdd8?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8Y2FyfGVufDB8fDB8fA%3D%3D&w=1000&q=80"
        result = GetImageCaption(img_src)
        expected_result = "a black sports car parked on a road"
        if not result:
            self.fail("No caption generated")
        self.assertEqual(result.get("result"), expected_result)

    def test_caption_book(self):
        img_src = "https://cdn.elearningindustry.com/wp-content/uploads/2016/05/top-10-books-every-college-student-read-1024x640.jpeg"
        result = GetImageCaption(img_src)
        expected_result = "a stack of books with a bookmark"
        if not result:
            self.fail("No caption generated")
        self.assertEqual(result.get("result"), expected_result)

    def test_caption_flowers(self):
        img_src = "https://flowersandfancies.imgix.net/images/itemVariation/EndlessSunflowersMedium-220421110614.jpg?auto=format&w=375&h=450&fit=crop"
        result = GetImageCaption(img_src)
        expected_result = "a vase of sunflowers on a table"
        if not result:
            self.fail("No caption generated")
        self.assertEqual(result.get("result"), expected_result)

    def test_caption_text(self):
        img_src = "https://i.pinimg.com/originals/fc/42/68/fc426877b77a4f8954f9231660efad36.jpg"
        result = GetImageCaption(img_src)
        expected_result = "a person with a blue shirt: Information technology and business are becoming inextricably interwoven. I don't think anybody can talk meaningfully about one without the talking about the other. (Bill Gates) izquotes.com"
        if not result:
            self.fail("No caption generated")
        self.assertEqual(result.get("result"), expected_result)


if __name__ == "__main__":
    unittest.main()
