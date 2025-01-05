import React from "react";
import styles from '../css/main.module.css';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrashCan } from '@fortawesome/free-solid-svg-icons';
const Main = () => {
    return (
        <main className={styles.mainArea}>
            <div className={styles.timeArea}>24년 1월 04일</div>
            <div className={styles.textBoxesArea}>
                <div className={`${styles.leftTextBox} ${styles.textBox}`}>
                    <textarea className={styles.textArea}></textarea>
                    <div className={`${styles.throwBtn} ${styles.btns}`}>버리기</div>
                </div>
                <div className={`${styles.rightTextBox} ${styles.textBox}`}>
                    <textarea className={styles.textArea}></textarea>
                    <div className={`${styles.againBtn} ${styles.btns}`}>다시쓰기</div>
                </div>
            </div>
            <footer className={styles.trashCanArea}>
                <FontAwesomeIcon icon={faTrashCan} className={styles.trashCan} />
            </footer>
        </main>
    )
}

export default Main;