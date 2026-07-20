import streamlit as st

# إعداد الصفحة
st.set_page_config(
    page_title="لعبة تحدي الذاكرة",
    page_icon="🎮",
    layout="centered"
)

# عنوان اللعبة
st.title("🎮 لعبة تحدي الذاكرة")

st.write("""
مرحباً بكِ في لعبة تحدي الذاكرة!

تحتوي اللعبة على 4 مراحل:

- المبتدئ
- المحترف
- الخبير
- النهائية
""")

# عرض معلومات المراحل
levels = [
    {
        "name": "المبتدئ",
        "time": 40,
        "attempts": 20,
    },
    {
        "name": "المحترف",
        "time": 50,
        "attempts": 25,
    },
    {
        "name": "الخبير",
        "time": 60,
        "attempts": 30,
    },
    {
        "name": "النهائية",
        "time": 70,
        "attempts": 35,
    }
]

st.subheader("معلومات المراحل")

for i, level in enumerate(levels, start=1):
    st.markdown(
        f"""
        ### المرحلة {i} : {level["name"]}

        - الزمن: {level["time"]} ثانية
        - عدد المحاولات: {level["attempts"]}
        """
    )

# زر بدء اللعبة
if st.button("ابدئي اللعب"):
    st.success("تم بدء اللعبة بنجاح! 🎉")
    st.balloons()

st.divider()

st.write("تم إنشاء اللعبة باستخدام Python و Streamlit.")
