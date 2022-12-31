import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.utils import load_img, img_to_array



new_model = tf.keras.models.load_model("C:\\Users\\VO PHU\\Desktop\\DANH\\30monan.h5")


def load_img():
    global img, image_data
    for img_display in frame.winfo_children():
        img_display.destroy()
    

    image_data = filedialog.askopenfilename(initialdir="/", title="Choose an image",
                                       filetypes=(("all files", "*.*"), ("png files", "*.png")))
    basewidth = 200 # Processing image for displaying
    img = Image.open(image_data)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    panel_image = tk.Label(frame, image=img).pack()

    

def classify():
    original = Image.open(image_data)
    original = original.resize((150, 150), Image.ANTIALIAS)
    numpy_image = img_to_array(original)
    image_batch = np.expand_dims(numpy_image, axis=0)
    result = new_model.predict(image_batch)
    global prediction, thongtinmonan, loaimonan 
    
    if round(result[0][0]) == 1:
        prediction = 'Bánh bèo'
    if round(result[0][1]) == 1:
        prediction = 'Bánh bột lọc'
    if round(result[0][2]) == 1:
        prediction = 'Bánh căn'
    if round(result[0][3]) == 1:
        prediction = 'Banh canh'
    if round(result[0][4]) == 1:
        prediction = 'Bánh chưng'
    if round(result[0][5]) == 1:
        prediction = 'Bánh cuốn'
    if round(result[0][6]) == 1:
        prediction = 'Bánh đúc'
    if round(result[0][7]) == 1:
        prediction = 'Bánh giò'
    if round(result[0][8]) == 1:
        prediction = 'Bánh khọt'
    if round(result[0][9]) == 1:
        prediction = 'Bánh mì'
    if round(result[0][10]) == 1:
        prediction = 'Bánh pía'
    if round(result[0][11]) == 1:
        prediction = 'Bánh tét'
    if round(result[0][12]) == 1:
        prediction = 'Bánh tráng nướng'
    if round(result[0][13]) == 1:
        prediction = 'Bánh xèo'
    if round(result[0][14]) == 1:
        prediction = 'Bún bò huế'
    if round(result[0][15]) == 1:
        prediction = 'Bún đậu mắm tôm'
    if round(result[0][16]) == 1:
        prediction = 'Bún mắm'
    if round(result[0][17]) == 1:
        prediction = 'Bún riêu'
    if round(result[0][18]) == 1:
        prediction = 'Bún thịt nướng'
    if round(result[0][19]) == 1:
        prediction = 'Cá kho tộ'
    if round(result[0][20]) == 1:
        prediction = 'Canh chua'
    if round(result[0][21]) == 1:
        prediction = 'Cao lầu'
    if round(result[0][22]) == 1:
        prediction = 'Cháo lòng'
    if round(result[0][23]) == 1:
        prediction = 'Cơm tấm'
    if round(result[0][24]) == 1:
        prediction = 'Gỏi cuốn'
    if round(result[0][25]) == 1:
        prediction = 'Hủ tiếu'
    if round(result[0][26]) == 1:
        prediction = 'Mì Quảng'
    if round(result[0][27]) == 1:
        prediction = 'nem chua'
    if round(result[0][28]) == 1:
        prediction = 'Phở'
    if round(result[0][29]) == 1:
        prediction = 'Xôi xéo'

    print("Đây là :", str(prediction).upper())
    
    d = {"Bánh Bèo":"Bánh bèo đã trở thành một nét đẹp trong văn hóa ẩm thực của người dân Viêt Nam từ bao đời nay. Bánh bèo là sự kết hợp của 3 yếu tố chính đó là bánh làm từ bột gạo, nhân để rắc lên bánh làm bằng tôm xay nhuyễn, và nước chấm. Nước chấm bánh bèo là một hỗn hợp với thành phần chính là nước mắm và thường đổ trực tiếp vào bánh chứ không cần chấm. ",
    "Bánh bột lọc":"Bánh bột lọc là loại bánh bao bột sắn nhỏ, trong, dai trong ẩm thực Việt Nam, có thể dùng làm món khai vị hoặc ăn vặt. Chúng thường chứa đầy tôm và bụng heo, thường được phủ lên trên với hẹ tây chiên và chấm với nước mắm ớt ngọt","Bánh căn":"Bánh căn là một loại bánh phổ biến của Ninh Thuận, Bình Thuận . Sau này được phát triển ở vùng Nam Trung Bộ, đặc biệt ở các tỉnh Khánh Hòa, Lâm Đồng, Bình Thuận. Bánh căn có hình dáng gần với bánh khọt ở các tỉnh phía Nam, nhưng cách làm hoàn toàn khác. Nếu như bánh khọt là loại bột gạo chiên (vì có dùng dầu mỡ) thì bánh căn là loại bột gạo nướng. Làm bánh căn thường phải có khuôn đúc đặc biệt, thường làm bằng đất nung, và có nhiều lỗ tròn để đặt khuôn. Vì bánh căn nhỏ nên thường tính theo cặp chứ không theo cái, ở giữa có thể quét mỡ hành hoặc đổ trứng. Bánh căn thường ít được dọn cùng rau sống ăn lá, mà thường ăn kèm với xoài xanh, khế chua, dưa leo băm sợi",
    "Banh canh":"Bánh canh là một loại mì đặc của Việt Nam, có thể được làm từ bột sắn hoặc hỗn hợp gạo và bột sắn. Bánh dùng để chỉ một tấm bột dày chưa nấu chín dùng để cắt sợi mì. Bánh canh cua - một loại súp cua đậm đà, thường có thêm trứng cút. Bánh canh bột lọc - một phiên bản mì trong mờ và dai hơn",
    "Bánh Chưng":"Bánh chưng là một loại bánh truyền thống của dân tộc Việt nhằm thể hiện lòng biết ơn của con cháu đối với cha ông với đất trời. Nguyên liệu làm bánh chưng gồm gạo nếp, đậu xanh, thịt lợn, lá dong. Bánh thường được làm vào các dịp Tết của dân tộc Việt, cũng như ngày giỗ tổ Hùng Vương",
    "Bánh cuốn":"Bánh cuốn, còn gọi là bánh mướt hay bánh ướt (khi không có nhân),là một món ăn làm từ bột gạo hấp tráng mỏng, cuộn tròn, bên trong độn nhân rau hoặc thịt",
    "Bánh đúc":"Bánh đúc là một loại bánh của Việt Nam, thường được làm bằng bột gạo (tại miền Bắc và miền Trung) hoặc bột năng (miền Nam) với một số gia vị. Bánh được làm thành tấm to, khi ăn thì cắt nhỏ thành miếng tùy thích.Là món ăn dân dã thịnh hành khắp ba miền, bánh đúc ăn giòn, mát, mịn, no bụng mà lại dễ tiêu, dễ làm và giá thành cũng rất rẻ. Không chỉ được ăn như một thức quà quê, bữa ăn sáng mà điển hình là bánh đúc chấm tương, bánh đúc cũng có thể ăn kèm với canh riêu cua, rau thơm, mắm tôm, mật ong, mật mía, mứt trái cây và thậm chí cả cá kho, thịt kho tùy thích",
    "Bánh giò":"Bánh giò là một loại bánh được làm bằng bột gạo tẻ, bột năng hòa với nước xương hầm, nhân làm từ thịt nạc vai có kèm mộc nhĩ, hành tím khô, hành ta, hạt tiêu, nước mắm, muối, (ở Miền Nam nhân bánh còn có thêm trứng cút) Bánh giò có hình dài nhô cao như hình bàn tay úp khum khum với các ngón tay sát nhau, bánh được gói bằng lá chuối và hấp bằng chõ từ 30 đến 40 phút.",
    "Bánh Khọt":"Bánh khọt là loại bánh Việt Nam (chính xác là loại bánh đặc trưng của miền nam Việt Nam) làm từ bột gạo hoặc bột sắn, có nhân tôm, được nướng và ăn kèm với rau sống, ớt tươi, thường ăn với nước mắm pha ngọt, rất ít khi chấm nước sốt mắm tôm (không phải mắm tôm hay mắm tôm chua).",
    "Bánh mì":"Bánh mì Việt Nam (gọi tắt là bánh mì) là một món ăn Việt Nam, với lớp vỏ ngoài là một ổ bánh mì nướng có da giòn, ruột mềm, còn bên trong là phần nhân. Tùy theo văn hóa vùng miền hoặc sở thích cá nhân, người ta có thể chọn nhiều nhân bánh mì khác nhau. Tuy nhiên, loại nhân bánh truyền thống thường chứa chả lụa, thịt, cá, thực phẩm chay hoặc mứt trái cây, kèm theo một số nguyên liệu phụ khác như patê, bơ, rau, ớt và đồ chua. Bánh mì được xem như một loại thức ăn nhanh bình dân và thường được tiêu thụ trong bữa sáng hoặc bất kỳ bữa phụ nào trong ngày.",
    "Bánh pía":"Bánh pía (tiếng Trung: 朥饼; Bạch thoại tự: hó-piáⁿ là món bánh ngọt ngàn lớp có nhân và là bánh trung thu truyền thống xuất phát từ Triều Châu, Trung Quốc và được du nhập vào các khu phố người Hoa trên thế giới. Đặc biệt ở Đông Nam Á, nơi có Hoa Kiều cư ngụ là Malaysia, Indonesia, Philippines và Singapore. Ở Indonesia, bánh có tên gọi là Bakpia Pathok.Tại Việt Nam, bánh pía là một trong những đặc sản của Sóc Trăng, do người Hoa di cư vào miền Nam sáng tạo ra. Bánh pía được làm từ bột mì nhào mỡ nước từ heo.",
    "Bánh tét":"Bánh tét, có nơi gọi là bánh đòn, là một loại bánh trong ẩm thực của cả người Việt và một số dân tộc ít người ở miền Nam và miền Trung Việt Nam, là nét tương đồng của bánh chưng ở Miền Bắc về nguyên liệu, cách nấu, chỉ khác về hình dáng và sử dụng lá chuối để gói thay vì lá dong, vì vậy nó cũng được sử dụng nhiều nhất trong dịp Tết Nguyên đán cổ truyền của dân tộc Việt Nam với vị trí không khác bánh chưng. Nhưng cũng có nhiều bánh tét nhân chuối hay đậu đen được làm hay là bán quanh năm",
    "Bánh tráng nướng":"Bánh tráng nướng là một món ăn nhẹ có xuất xứ từ Phan Rang (Ninh Thuận), sau đó rộng rãi ở Đà Lạt, Phan Thiết và phổ biến tại Sài Gòn. Nó được làm từ loại bánh tráng mỏng nướng giòn với phần nhân bánh phong phú như xúc xích, gà xé, thập cẩm, hải sản, khô bò, phô mai, trứng gà..., tương tự như kiểu bánh pizza của Ý và rưới kèm nước sốt (tương ớt và sốt me)",
    "Bánh xèo":"Bánh xèo là một loại bánh phổ biến ở châu Á, phiên bản bánh xèo của Nhật Bản và Triều Tiên có bột bên ngoài, bên trong có nhân là tôm, thịt, giá đỗ, kim chi, khoai tây, hẹ, (bánh xèo Triều Tiên); tôm, thịt, cải thảo (Nhật Bản) được rán màu vàng, đúc thành hình tròn hoặc gấp lại thành hình bán nguyệt. Tuỳ theo từng địa phương tại Việt Nam mà bánh được thưởng thức với nét đặc trưng riêng. Thường có 2 phương pháp chính: đổ bánh xèo giòn và bánh xèo dai. Ăn bằng hai cách: ăn bốc hoặc ăn bằng đũa.Tại miền Nam Việt Nam, bánh có cho thêm trứng và người ta ăn bánh xèo chấm nước mắm chua ngọt. Tại miền Bắc Việt Nam, nhân bánh xèo ngoài các thành phần như các nơi khác còn thêm củ đậu thái mỏng hoặc khoai môn thái sợi.",
    "Bún bò Huế":"Bún bò là một trong những đặc sản của xứ Huế, mặc dù món bún này phổ biến trên cả ba miền ở Việt Nam và cả người Việt tại hải ngoại. Tại Huế, món này được gọi đơn giản là bún bò hoặc gọi cụ thể hơn là bún bò thịt bò. Các địa phương khác gọi là bún bò Huế,bún bò gốc Huế để chỉ xuất xứ của món ăn này. Món ăn có nguyên liệu chính là bún, thịt bắp bò, giò heo, cùng nước dùng có màu đỏ đặc trưng và vị sả và ruốc. Đôi khi tô bún còn được thêm vào thịt bò tái, chả cua, và các loại nguyên liệu khác tùy theo sở thích của người nấu",
    "Bún đậu mắm tôm":"Bún đậu mắm tôm là món ăn đơn giản, dân dã trong ẩm thực miền Bắc Việt Nam. Đây là món thường được dùng như bữa ăn nhẹ, ăn chơi. Thành phần chính gồm có bún tươi, đậu hũ chiên vàng, chả cốm, nem chua,dồi chó, mắm tôm pha chanh, ớt và ăn kèm với các loại rau thơm như tía tô, kinh giới, rau húng, xà lách, cà pháo.. Cũng như các món ăn dân gian khác, giá thành rẻ nên được nhiều người giới bình dân ăn nên thu nhập của những người buôn bán những món ăn này khá cao",
    "Bún riêu":"Bún riêu là một món ăn truyền thống Việt Nam, được biết đến rộng rãi trong nước và quốc tế. Món ăn này gồm bún (bún rối hoặc bún lá) và riêu cua'. Riêu cua là canh chua được nấu từ gạch cua, thịt cua giã và lọc cùng với quả dọc, cà chua, mỡ nước, giấm bỗng, nước mắm, muối, hành hoa. Bún riêu thường thêm chút mắm tôm để tăng thêm vị đậm đà, thường ăn kèm với rau sống. Đây là món ăn có vị chua thanh, ăn vào mùa hè rất mát nên được người Việt rất ưa thích. Trên các đường phố của Việt Nam có rất nhiều hàng quán bán bún riêu.",
    "Bún thịt nướng":"Bún thịt nướng là một món ăn có nguồn gốc ở miền Nam Việt Nam, về sau đã phổ biến lan rộng tại nhiều nơi trên cả nước. Mỗi nơi đều có thể có cho mình một hương vị đặc trưng riêng tùy theo khẩu vị từng nơi. Món bún này có thể dùng làm điểm tâm, bữa chính hay bữa phụ đều phù hợp. Yêu cầu của món Bún thịt nướng là thịt được nướng vàng đều, có vị đậm đà cùng hương thơm của sả và vừng; nước mắm chua ngọt vừa ăn; và các loại rau dùng kèm đa dạng.",
    "Cá kho tộ":"Cá kho tộ vốn là món ăn dân dã của người dân vùng sông nước miền tây nam bộ. Thường xuất hiện trong bữa cơm hàng ngày của nhiều gia đình, những niêu cá kho chinh phục người ăn bằng hương vị đậm đà, béo ngậy, thơm ngon và đặc biệt “tốn cơm”",
    "Canh chua":"Canh chua là tên gọi của những món ăn nhiều nước và có vị chua do được nấu bằng các nguyên liệu phối trộn với gia vị tạo chua. Canh chua thường được dùng ở những vùng nóng như miền Nam, miền Trung, hoặc những lúc nóng nực của mùa hè miền Bắc Việt Nam, món canh chua này cũng đặc biệt phổ biến trong nghệ thuật ẩm thực Hà Nội",
    "Cao lầu":"Cao lầu là một món mì ở Quảng Nam, Việt Nam. Đây được xem là món ăn đặc sản của thành phố Hội An. Món mì này có sợi mì màu vàng, được dùng với tôm, thịt heo, các loại rau sống và rất ít nước dùng. Sợi mì màu vàng là do được trộn với tro từ một loại cây ở địa phương",
    "Cháo lòng":"Cháo lòng là món cháo được nấu theo phương thức nấu cháo thông thường, trong sự kết hợp với nước dùng ngọt làm từ xương lợn hay nước luộc lòng lợn, và nguyên liệu chính cho bát cháo không thể thiếu các món phủ tạng lợn luộc, dồi. Cháo lòng tương đối phổ thông thậm chí khá bình dân trong ẩm thực Việt Nam, được bán rộng rãi tại các cửa hàng lòng lợn trong cả nước, tạo nên một bộ ba sản phẩm được ăn theo thứ tự trong bữa ăn là tiết canh, lòng lợn, cháo lòng, và thường kết hợp với rượu đế.",
    "Cơm tấm":"Cơm tấm, cơm sườn, hay Cơm tấm Sài Gòn là một món ăn Việt Nam có nguyên liệu chủ yếu từ gạo tấm. Dù có nhiều tên gọi ở các vùng miền khác nhau, tuy nhiên nguyên liệu và cách thức chế biến của món ăn trên gần như là giống nhau.Thành phần chính bao gồm Gạo tấm, sườn nướng, nước mắm pha, đồ chua, dưa leo, cà chua, mỡ hành.",
    "Gỏi cuốn":"Gỏi cuốn hay còn được gọi là nem cuốn (phương ngữ Bắc bộ), là một món ăn khá phổ biến ở Việt Nam.Gỏi cuốn có xuất xứ từ Miền nam Việt Nam với tên gọi là gỏi cuốn - bằng các nguyên liệu gồm rau xà lách, húng quế, tía tô, tôm khô, rau thơm, thịt luộc, tôm tươi.. tất cả được cuộn trong vỏ bánh tráng. Gia vị dùng kèm là tương hột trộn với lạc rang giã nhỏ phi bằng dầu ăn với hành khô.... tất cả thái nhỏ và cuộn trong vỏ làm từ bột mì. Gia vị dùng kèm là tương ớt trộn với lạc rang giã nhỏ phi bằng dầu ăn với hành khô.",
    "Hủ tiếu":"Hủ tiếu phát triển rất mạnh ở miền Nam Việt Nam từ những năm 50, đặc biệt là tại Sài Gòn, rất dễ tìm thấy quán hủ tiếu trên đường phố hoặc xe hủ tiếu đẩy ở đầu hẻm.Có thể nói Hủ tiếu là món ăn đặc trưng tại đây, tương tự như phở ở Hà Nội hay bún bò tại Huế. Hủ tiếu thường là món ăn sáng hoặc ăn tối, người miền Nam ít ăn trưa với hủ tiếu.Nguyên liệu chính của món hủ tiếu là bánh hủ tiếu, nước dùng chính là với thịt bằm nhỏ, lòng heo nấu cùng. Sau đó trụng sơ bánh hủ tiếu với nước dùng, rồi cho các nguyên liệu phụ vào như giá đỗ, hẹ, thịt bằm vào. Có thể ăn với thịt bò viên và tương ớt, tương đen.",
    "Mì Quảng":"Mỳ Quảng là một món ăn đặc sản đặc trưng của Quảng Nam và Đà Nẵng, Việt Nam.Mỳ Quảng thường được làm từ bột gạo xay mịn với nước từ hạt dành dành và trứng cho có màu vàng và tráng thành từng lớp bánh mỏng, sau đó thái theo chiều ngang để có những sợi mỳ mỏng khoảng 5 -10mm.Dưới lớp mỳ là các loại rau sống, Mỳ Quảng phải ăn kèm với rau sống 9 vị thì mới tạo nên được hương vị nồng nàn: húng quế, xà lách tươi, cải non mới nụ, giá trắng có thể được trụng chín hoặc để sống, ngò rí, rau răm với hành hoa thái nhỏ và thêm hoa chuối cắt mỏng.Trên mỳ là thịt lợn, tôm, thịt gà, thịt cá lóc (đôi khi có trứng luộc) cùng với nước dùng được hầm từ xương heo. Người ta còn bỏ thêm lạc rang khô và giã dập, hành lá thái nhỏ, rau thơm, ớt đỏ... Thông thường nước dùng được gọi là nước nhưng đây cũng là một loại nước lèo nhưng rất cô đặc và ít nước.Ngoài ra mỳ còn được dùng kèm với bánh tráng mè, thêm cả đậu phộng rang giòn thơm tạo nên hương vị đặc trưng",
    "nem chua":"Nem chua (phương ngữ Bắc Bộ) hay nem (phương ngữ Trung Bộ và phương ngữ Nam Bộ) là một món ăn sử dụng thịt lợn, lợi dụng men của lá chuối (hoặc lá ổi, lá vông, lá sung v.v.) và thính gạo để ủ chín, có vị chua ngậy. Nổi tiếng ở Việt Nam như một sản vật phổ biến tại nhiều địa phương, tuy không rõ nem chua được người dân vùng nào làm ra đầu tiên. Cách chế biến nem có thể chia thành hai kiểu: Nem Miền Bắc có thể chế biến ăn sống cùng các loại lá đặc biệt; còn Nem Miền Trung (đặc biệt Thanh Hoá và Huế) được đóng gói và lên men trong một số loại lá, trong đó có lá chuối, lá ổi.",
    "Phở":"Phở là một món ăn truyền thống của Việt Nam, có nguồn gốc từ Nam Định, Hà Nội và được xem là một trong những món ăn tiêu biểu cho nền ẩm thực Việt Nam.Thành phần chính của phở là bánh phở và nước dùng cùng với thịt bò hoặc thịt gà cắt lát mỏng. Thịt bò thích hợp nhất để nấu phở là thịt, xương từ các giống bò ta (bò nội, bò vàng). Ngoài ra còn kèm theo các gia vị như: tương, tiêu, chanh, nước mắm, ớt, vân vân. Những gia vị này được thêm vào tùy theo khẩu vị của người dùng. Phở thông thường được dùng để làm món điểm tâm buổi sáng hoặc lót dạ buổi đêm; nhưng ở các thành phố lớn, món ăn này có thể được thưởng thức cả ngày.",
    "Xôi xéo":"Xôi xéo là món xôi quen thuộc của người Hà Nội, mỗi khi nhắc tới là gợi đến ngay màu sắc vàng của xôi rất đặc trưng. Công đoạn nấu xôi xéo khá tốn nhiều thời gian từ việc chọn gạo nếp cho đến thành phẩm trưng bày.Cụ thể, người nấu phải chọn loại nếp cái hoa vàng thơm ngon, rồi ngâm với nước ấm khoảng 5 tiếng trước khi nấu xôi. Ngoài ra, chọn loại đậu xanh ruột vàng (bỏ vỏ), xay vỡ đôi hạt và cũng đem ngâm vào trong nước ấm chừng 2 tiếng rồi mới mang đi nấu chín kèm với ít muối. Sau khi đậu xanh chín, dùng đũa đánh tơi mịn và nắm chặt đậu thành từng nắm.Khi ăn, xới xôi ra đĩa, rồi dùng dao thái mỏng lát đậu xanh và phủ lên trên, rưới thêm nước mỡ gà và rắc hành phi vàng."}

    
    thongtinmonan = tk.Message(wd, bg= 'azure', justify= 'center', text= str(d[prediction]),relief=RAISED)
    thongtinmonan.place(x = 280, y = 130,width= 600)
    
    loaimonan = tk.Label(wd, text = str(prediction).upper(), bg = '#F0F0F0',fg = 'sienna', font= ("", 24))
    loaimonan.place(x= 400, y = 60)

    
#GIAO DIEN
wd = Tk()
wd.title('NHẬN DIỆN 30 MÓN ĂN CỦA VIỆT NAM')
wd.geometry('900x500')
wd.configure(bg='lavender')
wd.resizable(width=False, height=False)

frame = Frame(wd)
frame['bg'] = 'Black'
frame['bd'] = 5
frame.place(x=60, y =60, width = 200, height = 200)


Label1=tk.Label(wd,text=" MÓN ĂN VIỆT NAM :",fg='black',font=("Arial",14),justify="center",bg='lavender')
Label1.place(x=0,y=0,width=900,height=50)
Label2=tk.Label(wd,text=" ĐÂY LÀ :",fg='black',font=("Arial",14),justify="right")
Label2.place(x=280,y=80,width=100,height=25)


Button1=tk.Button(wd,text='IMAGE OPEN',bg='cornsilk',font=('Arial',14),justify='center',command=load_img)
Button1.place(x=50,y=350,width=800,height=35)
Button2=tk.Button(wd,text='CALSSIFY',fg='#000000',bg='cyan',font=('Arial',14),justify='center',command=classify)
Button2.place(x=50,y=420,width=800,height=35)



wd.mainloop()